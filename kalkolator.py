from classes import kalkolator


def kalkolators():
    serveses = input("""
        1.*
        2./
        3.+
        4.-
         >>>""")
    if serveses == '1':
        print(kalkolator.kopaytirish())
        return kalkolators()

    elif serveses == '2':
        print(kalkolator.bolish())
        return kalkolators()

    elif serveses == '3':
        print(kalkolator.qoshish())
        return kalkolators()

    elif serveses == '4':
        print(kalkolator.ayrish())
        return kalkolators()

    else:
        print("Bunday amal mavjud emas:")
        return kalkolators()


if __name__ == '__main__':
    kalkolators()