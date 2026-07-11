import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        self.ini_data = {section: dict(self.config[section]) for section in self.config.keys()}
        # print(f'self.ini_data is {self.ini_data}')

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/articles/property-decorator
        """
        # print(f'sections are {self.config.sections()}')
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        # print(f'list of environments is {self.ini_data['tox']}')
        # print(f'type of list of environments is {type(self.ini_data['tox'])}')
        ret_val = self.ini_data['tox']['envlist'].strip().split('\n')
        print(f'type ret_val is {type(ret_val)}')
        print(f'ret_val is {ret_val}')
        print(f'sorted(ret_val) is {sorted(ret_val)}')
        return ret_val

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        bases = set()
        for section_name in self.config.keys():
            for key, value in self.config[section_name].items():
                if key == 'basepython':
                    bases.add(value)
        # print(bases)
        return list(bases)


if __name__ == '__main__':
    tip = ToxIniParser('/tmp/django-tox.ini')
    print(f'in main(), tip.number_of_sections is {tip.number_of_sections}')
    print(f'in main(), tip.environments is {tip.environments}')
    print(f'in main(), sorted(tip.environments is {sorted(tip.environments)}')
    print(f'in main(), type(tip.environments) is {type(tip.environments)}')
    print(f'in main(), tip.base_python_versions is {tip.base_python_versions}')