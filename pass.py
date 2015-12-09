import grampg

""" simple utility to create an LDAP password for aegir-service account """

def genpass(quantity):
    password = grampg.PasswordGenerator()

    generator = (password.of()
                 .exactly(10, 'lower_letters')
                 .exactly(5, 'numbers')
                 .at_least(5, 'upper_letters')
                 .beginning_with('lower_letters')
                 .done())
    for i in range(quantity):
        return generator.generate()


mypass = genpass(1)

if __name__ == '__main__':
    genpass(1)
