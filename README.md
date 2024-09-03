# Micropython Dev Environment

Minimal Micropython project template used on WSL, with rshell & micropython-rp2-pico-w-stubs.

This repository uses a forked rshell version, which fixes an incorrect check for WSL environment due to a non-capitalised
'Microsoft' in Python `platform.uname().release` string value.

- The `rshell` package is used to transfer files to and from the Raspberry Pi device and access the REPL.
- The `micropython-rp2-pico-w-stubs` package enables Micropython type hints and intellisense in VSCode.
