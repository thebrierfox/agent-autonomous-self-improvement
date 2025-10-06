from pathlib import Path

def main():
    kit_file = Path('handoff_kit.txt')
    if kit_file.exists():
        print(kit_file.read_text())
    else:
        print('handoff_kit.txt not found')

if __name__ == '__main__':
    main()
