from .args import prepare_parser


def main():
    print(vars(prepare_parser()))
