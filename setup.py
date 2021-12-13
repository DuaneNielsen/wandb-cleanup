from setuptools import setup

setup(name='wandb-cleanup',
      version='0.1',
      description='Cleanup wandb artifacts',
      url='http://github.com/duanenielsen/wandb-cleanup',
      author='duanenielsen',
      author_email='duane.nielsen.rocks@gmail.com',
      license='MIT',
      packages=['wandb_cleanup'],
      scripts=['bin/wandb-cleanup'],
      zip_safe=False)