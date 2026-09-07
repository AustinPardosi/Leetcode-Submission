class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            char = chars[read]
            start = read

            while read < len(chars) and (char == chars[read]):
                read += 1

            chars[write] = char
            write += 1
            count = read - start

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write