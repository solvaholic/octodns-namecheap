from setuptools import find_packages, setup


def descriptions():
    with open('README.md') as fh:
        ret = fh.read()
        first = ret.split('\n', 1)[0].replace('#', '')
        return first, ret


def version():
    with open('octodns_namecheap/__init__.py') as fh:
        for line in fh:
            if line.startswith('__VERSION__'):
                return line.split("'")[1]


description, long_description = descriptions()

setup(
    author='Roger D. Winans',
    author_email='mr.winans@gmail.com',
    description=description,
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='octodns-namecheap',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=(
        'octodns>=0.9.14',
        # TODO: other requirements
    ),
    url='https://github.com/octodns/octodns-namecheap',
    version=version(),
    tests_require=(
        'pytest',
        'pytest-network',
        # TODO: other test-time requirements
    ),
)
