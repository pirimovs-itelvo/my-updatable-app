import subprocess

def main():
    print("hi!")

if __name__ == "__main__":
    # Run the update script before starting the main program
    subprocess.run(['python', 'update.py'])
    main()
