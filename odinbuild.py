#!/usr/bin/env python3
import subprocess
import os
import sys

def run_command(cmd, cwd=None):
    """Run a shell command and exit if it fails."""
    print(f"\nRunning: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error: Command failed -> {cmd}")
        sys.exit(1)

def reinstall_vscode_git():
    print("\n[1] Reinstalling VSCode and Git...")
    # Update package list
    run_command("sudo apt-get update")
    # Reinstall VSCode (installed as 'code') and git
    run_command("sudo apt-get install --reinstall code git -y")

def setup_git_accounts():
    print("\n[2] Setting up Git account configuration...")
    username = input("Enter your Git username: ").strip()
    email = input("Enter your Git email: ").strip()
    run_command(f'git config --global user.name "{username}"')
    run_command(f'git config --global user.email "{email}"')
    print("Git global configuration updated.")

def update_and_build_odin():
    print("\n[3] Updating and building Odin...")
    odin_dir = input("Enter the full path to your Odin project directory: ").strip()
    if not os.path.isdir(odin_dir):
        print(f"Error: Directory '{odin_dir}' does not exist. Exiting.")
        sys.exit(1)
    # Pull the latest changes from GitHub
    run_command("git pull origin main", cwd=odin_dir)
    # Check for the build script and run it if found
    build_script = os.path.join(odin_dir, "build_odin.sh")
    if os.path.isfile(build_script):
        # Ensure the build script is executable
        run_command(f"chmod +x {build_script}", cwd=odin_dir)
        run_command(f"./build_odin.sh", cwd=odin_dir)
    else:
        print("Warning: build_odin.sh not found in the specified directory.")

def main():
    print("Starting reinstallation and update process for VSCode, Git, and Odin...")
    reinstall_vscode_git()
    setup_git_accounts()
    update_and_build_odin()
    print("\nAll tasks completed successfully.")

if __name__ == "__main__":
    main()
