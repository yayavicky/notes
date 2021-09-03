```python
def get_command_2(self):
    other = []
    self.refresh_check_sum()
    for item in self._cmd_list:
        if isinstance(item, bytes):
            other.append(int.from_bytes(item, 'big'))
            else:
                other.append(item)
                print(other)
                rst = '\\X' + '\\x'.join('{:02X}'.format(x) for x in other)

                print(rst)

```

