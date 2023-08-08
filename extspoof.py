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

    
    input_data = argv2
    output_file = argv1
    # Encode the PDF file into a string
    with open(input_data, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")
    
    with open(output_file, "a") as new_code:
        new_code.write("\n\nimport base64\n\n")
        new_code.write("encoded_pdf = \"" + encoded_string + "\"\n\n")
        new_code.write("# Decode the PDF string back into bytes\n")
        new_code.write("decoded_pdf = base64.b64decode(encoded_pdf)\n\n")
        new_code.write("# Write the decoded PDF bytes into a new file\n")
        new_code.write("with open(\"decoded.pdf\", \"wb\") as pdf_file:\n")
        new_code.write("    pdf_file.write(decoded_pdf)\n")
    print("(ExtSpoof) - Success.")

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
