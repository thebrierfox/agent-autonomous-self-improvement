from pathlib import Path

def main():
    template_file = Path('run_report_template.txt')
    if template_file.exists():
        print(template_file.read_text())
    else:
        print('run_report_template.txt not found')

if __name__ == '__main__':
    main()
