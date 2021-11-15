from collections import namedtuple


def parse_input():
    def line_to_dict_entry(line):
        s = line.split(" ")
        min_n = int(s[0].split("-")[0])
        max_n = int(s[0].split("-")[1])
        char = s[1].replace(":", "")

        pw = {
            "password": s[2].replace("\n", ""),
            "policy": {"min": min_n, "max": max_n, "char": char},
        }

        return pw

    with open("day_02/input", "r") as fp:
        passwords = [line_to_dict_entry(l) for l in fp.readlines()]
    return passwords


def is_valid_password_char_count(password, character, min_count, max_count):
    """
    Valid if character appears in password:
        - at least min_count times
        - at most max_count times
    """
    char_count = password.count(character)
    return min_count <= char_count <= max_count


def is_valid_password_char_position(password, character, positions):
    """
    Valid if character appears in password:
        - in exactly one of the positions (1 indexed)
    """
    valid = password[positions[0] - 1] == character
    for p in positions[1:]:
        valid = valid != (password[p - 1] == character)
    return valid


def parse_passwords():
    def extract_password(line):
        s = line.split(" ")
        return s[2].replace("\n", "")

    with open("day_02/input", "r") as fp:
        passwords = [extract_password(line) for line in fp.readlines()]
    return passwords


def parse_policies():
    Policy = namedtuple("Policy", ["a", "b", "char"])

    def extract_policy(line):
        s = line.split(" ")
        a = int(s[0].split("-")[0])
        b = int(s[0].split("-")[1])
        char = s[1].replace(":", "")
        return Policy(a, b, char)

    with open("day_02/input", "r") as fp:
        policies = [extract_policy(line) for line in fp.readlines()]
    return policies


if __name__ == "__main__":
    passwords = parse_passwords()
    policies = parse_policies()
    valid_pws = 0

    with open("day_02/input", "r") as fp:
        gen = fp.readlines()
        pass

    valid_pws_count = sum(
        [
            is_valid_password_char_count(pw_string, policy.char, policy.a, policy.b)
            for pw_string, policy in zip(passwords, policies)
        ]
    )

    valid_pws_pos = sum(
        [
            is_valid_password_char_position(
                pw_string, policy.char, [policy.a, policy.b]
            )
            for pw_string, policy in zip(passwords, policies)
        ]
    )

    print(f"Number of valid passwords: {valid_pws_count}")
