import re
import sys

ISSUE_URL_TEMPLATE = '<a href="https://github.com/liepieshov/liepieshov/issues/new?title=move:{}&template=custom.md">&nbsp;</a>'


class State:
    def __init__(self, encoded: str):
        assert len(encoded) == 9
        x_count = encoded.count("x")
        o_count = encoded.count("o")
        self.x_to_move = x_count <= o_count
        self.encoded = list(encoded)

    @property
    def sign_to_move(self):
        return "x" if self.x_to_move else "o"

    def format_cell(self, idx: int):
        assert 0 <= idx < 9
        if self.encoded[idx] == "o" or self.encoded[idx] == "x":
            return self.encoded[idx]
        encoded = self.encoded[:]
        encoded[idx] = self.sign_to_move
        return ISSUE_URL_TEMPLATE.format("".join(encoded))

    @property
    def is_winning(self):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        for x, y, z in (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ):
            if (self.encoded[x] == self.encoded[y] == self.encoded[z]) and (
                self.encoded[x] in "ox"
            ):
                return True
        return False

    def __str__(self) -> str:
        if self.is_winning:
            state = State("-" * 9)
            to_move = state.sign_to_move
            cells = [state.format_cell(i) for i in range(9)]
        else:
            to_move = self.sign_to_move
            cells = [self.format_cell(i) for i in range(9)]

        return """
## Play communal Tic Tac Toe with us🎲
`{}` to move (click the empty cell to move)

 <table>
  <tr>
    <th>{}</th>
    <th>{}</th>
    <th>{}</th>
  </tr>
  <tr></tr>
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
  <tr></tr>
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
</table>

""".format(
            to_move, *cells
        )


def main(title: str):
    if not re.match(r"^move\:[x|o|\-]{9}$", title):
        sys.exit(1)
    state = title.split(":")[1]
    print(State(state))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
