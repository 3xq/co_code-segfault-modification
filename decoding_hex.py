variables = vars()
unpacked = [*variables]

built_ins = unpacked[6]
built_ins = variables[built_ins].__dict__

unpacked_built_ins = [*built_ins]

lambda_hex = (lambda: '6b6f6d7423303030372c2068747470733a2f2f7777772e6769746875622e636f6d2f337871')

print_built_in = unpacked_built_ins[42]
bytes_built_in = unpacked_built_ins[57]

bytes_children = dir( built_ins[bytes_built_in] )

fromhex_built_in = bytes_children[40]
decode_built_in = bytes_children[36]

r"""

| t\x00     | LOAD_GLOBAL   | print                               |
| t\x01     | LOAD_GLOBAL   | byte                                |
| \xa0\x02  | LOAD_METHOD   | byte.fromhex                        |
| d\x01     | LOAD_CONSTANT | 6b6f6d ...                          |
| \xa1      | CALL_METHOD   | byte.fromhex('6b6f6d ...')          |
| \x01      | POP_TOP       |                                     |
| \xa0x03   | LOAD_METHOD   | byte.fromhex('6b6f6d ...').decode   |
| \xa1      | CALL_METHOD   | byte.fromhex('6b6f6d ...').decode() |
| \x00      | CACHE         |                                     |
| \x83      | CALL_FUNCTION | byte.fromhex('6b6f6d ...').decode() |
| \x01      | POP_TOP       |                                     |
| S\x00     | RETURN_VALUE  |                                     |


"""

exec(
    lambda_hex.__code__.replace(
        co_code = b't\x00t\x01\xa0\x02d\x01\xa1\x01\xa0\x03\xa1\x00\x83\x01S\x00',
        co_names = ( print_built_in, bytes_built_in, fromhex_built_in, decode_built_in )
    )
)
