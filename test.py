# import base64


# def encode(message: str) -> bytes:
#     """
#     Encode string for privacy and encryption.
#     """
#     msg_bytes = message.encode("latin-1")
#     string_bytes = base64.b64encode(msg_bytes)
#     string = string_bytes.decode("latin-1")
#     return string


# print(encode("test"))

# {
#     '{"info":{"1":["trtret","gerger"]},"yourdiv":"<div class': '\\"mb-3\\"><label for=\\"1-Label\\" class=\\"form-label\\"><input type=\\"text\\" class=\\"form-control\\" id=\\"1-Input-Name\\"></label><input type=\\"text\\" class=\\"form-control\\" id=\\"1-Content\\"></div>"}'
# }


# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b

# del tag["class"]
# del tag["id"]

# print(tag)


# print(str(all_input[0]), info[str(idx)][0])
# print(x)
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# del tag["class"]
# del tag["id"]
# print(tag)
# yourdiv.replace(str(all_input[0]), info[str(idx)][0])
from bs4 import BeautifulSoup, Tag

# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, "html.parser")
# a_tag = soup.a
# a_tag.string = "a"

# print(a_tag)
# new_tag = soup.new_tag("h1")
# new_tag.string = "example.com"
# a_tag.i.replace_with(new_tag)

# print(a_tag)

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, "html.parser")
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "example.com"
a_tag.i.replace_with(new_tag)
