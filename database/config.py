from configparser import ConfigParser


def config(filename, section='postgresql'):
    """ Read the config file to connect postgresql database
    """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    postgresql_data = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            postgresql_data[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(
            section,
            filename
        )
        )

    return postgresql_data
