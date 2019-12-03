import math as m
import decimal as dec


D = dec.Decimal

# Overkill but whatever
prec_pi = D(
    "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912")

dec.getcontext().prec = 600


# Get the accuracy in significant digits
# May be a little low for some super-accurate approximations involving transcendental functions like log, or even ones like sqrt()
def dec_accuracy(a: D, b: D):
    diff = abs((a - b))
    digits = diff.adjusted()
    return -digits - 1 if digits < 0 else 0


def show_pi_approx(name, approx: D):
    print("Approximation name: %s" % name)
    print("Approximation is accurate to %s decimal places" % dec_accuracy(approx, prec_pi))
    print()


approx_1 = (D(640320) ** 3 + D(744)).ln() / D(163).sqrt()

show_pi_approx("Heebler 163 natural log", approx_1)

approx_2 = ((D(5280) ** 3) *
            (D(236674) + D(30303) * D(61).sqrt()) ** 3
            + 744
            ).ln() / \
           D(427).sqrt()

show_pi_approx("J-invariant class 2 natural log", approx_2)


def quartu(v: D):
    return v + (v ** 2 - 1).sqrt()


half = D(1) / D(2)

sqrt2 = D(2).sqrt()

a = half * (D(23) + D(4) * D(34).sqrt())

b = half * (D(19) * sqrt2 + D(7) * D(17).sqrt())

c = (D(429) + D(304) * sqrt2)

d = half * (627 + 442 * sqrt2)

uu = quartu(a) ** 2 * \
     quartu(b) ** 2 * \
     quartu(c) * \
     quartu(d)

approx_3 = ((D(2) * uu) ** 6 + 24).ln() / D(3502).sqrt()

show_pi_approx("Dedekind Eta function modular", approx_3)
