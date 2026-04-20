from os.path import isfile
from shutil import copyfile


ALL_PATCHES = {
    "NAPOLEON": [
        {
            "8D 58 67 00 83 C4 08 B8 01":
            "8D 58 67 00 83 C4 08 B8 00"
        }
    ],
    "SHOGUN2": [
        {
            "FF FF 84 C0 BA 18 27 6D 11 B9 C0 5F 65 11 0F 44 CA":
            "FF FF 84 C0 BA 18 27 6D 11 B9 C0 5F 65 11 90 90 90"
        }
    ],
    "ROME2": [
        {
            "8B C8 E8 69 40 F3 FE 85 C0 74 2B 8B 8F 84 00 00 00 E8 BA EE FC FF 84 C0 75 1C":
            "8B C8 E8 69 40 F3 FE 85 C0 90 90 8B 8F 84 00 00 00 E8 BA EE FC FF 84 C0 90 90"
        }, {
            "8C 00 00 00 E8 A0 74 FC FF 84 C0 74 1E":
            "8C 00 00 00 E8 A0 74 FC FF 84 C0 90 90"
        }
    ],
    "ATTILA": [
        {
            "8C E4 BC FE 85 C0 74 25 8B 4F 58 E8 60 DE FD FF 84 C0 75 19":
            "8C E4 BC FE 85 C0 90 90 8B 4F 58 E8 60 DE FD FF 84 C0 90 90"
        }, {
            "60 8B CF E8 80 0D 08 00 84 C0 74 1B":
            "60 8B CF E8 80 0D 08 00 84 C0 90 90"
        }
    ]
}

# # Checks whether the orignal bytes are present or not
# def fileCheck(filename):
#     data = ''
#     with open(filename, 'rb') as input_file:
#         data = input_file.read()
#     for patch in PATCHES:
#         for original_bytes in patch.keys():
#             if data.find(bytearray.fromhex(original_bytes)) == -1:
#                 return False
#     return True

def apply_patches(filename, game):
    patches = ALL_PATCHES[game]

    data = ''
    with open(filename, 'rb') as input_file:
        data = input_file.read()

    success = True
    for patch in patches:
        for key, value in patch.items():
            occurences = data.count(bytearray.fromhex(key))
            if(occurences != 1):
                success = False
            
            data = data.replace(bytearray.fromhex(key), bytearray.fromhex(value))

    with open(filename, "wb") as output_file:
        output_file.write(data)

    return success