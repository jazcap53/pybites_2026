output = """
                                       mohh@SERENiTY
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        OS: Mint 19 tara
 MMm----::-://////////////oymNMd+'     Kernel: x86_64 Linux 4.15.0-34-generic
 MMd      /++                -sNMd:    Uptime: 1d 4m
 MMNso/'  dMM    '.::-. .-::.' .hMN:   Packages: 2351
 ddddMMh  dMM   :hNMNMNhNMNMNh: 'NMm   Shell: zsh 5.4.2
     NMm  dMM  .NMN/-+MMM+-/NMN' dMM   Resolution: 1366x768
     NMm  dMM  -MMm  'MMM   dMM. dMM   DE: Cinnamon 3.8.9
     NMm  dMM  -MMm  'MMM   dMM. dMM   WM: Muffin
     NMm  dMM  .mmd  'mmm   yMM. dMM   WM Theme: Linux Mint (Mint-Y)
     NMm  dMM'  ..'   ...   ydm. dMM   GTK Theme: Mint-Y [GTK2/3]
     hMM- +MMd/-------...-:sdds  dMM   Icon Theme: Mint-Y
     -NMm- :hNMNNNmdddddddddy/'  dMM   Font: Noto Sans 9
      -dMNs-''-::::-------.''    dMM   CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
       '/dMNmy+/:-------------:/yMMM   GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
          ./ydNMMMMMMMMMMMMMMMMMMMMM   RAM: 1886MiB / 6915MiB
             \.MMMMMMMMMMMMMMMMMMM    
"""


def sysinfo_scrape(output):
    """Scrapes the output from screenfetch and returns a dictionary"""
    lines = output.splitlines()
    if not lines:
        raise ValueError('no lines')
    ret = {}
    for line_num in range(len(lines)):
        line_offset = lines[line_num].rfind('  ') + 2
        sep_offset = lines[line_num].find(': ', line_offset)

        if line_offset > 2:
            break


    ret['Name'] = lines[line_num][line_offset:]
    for i in range(line_num + 1, len(lines)):
        value_pos = lines[i].find(':', line_offset) + 2
        if value_pos == 1:
            continue
        key_pos = lines[i].rfind(' ', value_pos) + 1
        key = lines[i][key_pos: value_pos].strip()
        ret[key] = lines[i][value_pos:].strip()
    return ret



if __name__ == '__main__':
    print(sysinfo_scrape(output))