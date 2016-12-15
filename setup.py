from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name='HomeIn',
            description='Exploration tool for previous house sales and crime rate in King County - a one-stop comp analysis.',
            long_description='Interactive multi-layer maps exploring previous house sales and crime rate in King Country '
                             'Layer 1: Individual selectable markers with desired house prices and specifications '
                             'Layer 2: Heatmap of crime rates'
                             'Layer 3: Choropleth map of house prices within each zip code.',
            license=open('LICENSE').read(),
            author='hanghu, jhp312, YangJiang89, MengyuanZoe',
            packages=PACKAGES,
            package_data={'HomeIn': ['Data/*.*']},
            include_package_data=True
            )

if __name__ == '__main__':
    setup(**opts)
