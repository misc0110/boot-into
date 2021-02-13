# boot-into

A small script to boot into a specific GRUB entry without changing the default boot option.

## Usage

Run the script as root. The script extracts all boot options from GRUB and lists them with a prepended ID. Enter the ID to boot into the respective entry, or "x" to abort. 

The computer reboots into the specified entry after entering the ID. 

## Example output

    > sudo python3 boot-into.py

    [ 0] Ubuntu
    [ 1] Ubuntu, with Linux 5.4.0-65-generic
    [ 2] Ubuntu, with Linux 5.4.0-65-generic (recovery mode)
    [ 3] Ubuntu, with Linux 5.4.0-64-generic
    [ 4] Ubuntu, with Linux 5.4.0-64-generic (recovery mode)
    [ 5] Ubuntu, with Linux 5.4.0-59-generic
    [ 6] Ubuntu, with Linux 5.4.0-59-generic (recovery mode)
    [ 7] Ubuntu, with Linux 5.4.0-37-generic
    [ 8] Ubuntu, with Linux 5.4.0-37-generic (recovery mode)
    [ 9] Ubuntu, with Linux 5.4.0-33-generic
    [10] Ubuntu, with Linux 5.4.0-33-generic (recovery mode)
    [11] Ubuntu, with Linux 5.4.0-21-generic
    [12] Ubuntu, with Linux 5.4.0-21-generic (recovery mode)
    [13] Windows Boot Manager (on /dev/nvme0n1p1)
    [14] UEFI Firmware Settings
    [ x] Quit
    Choice: 

