from setuptools import setup


setup(name='iosxr_grpc',
      version='1.2',
      description='gRPC library for IOS-XR > 6.1.1',
      url='https://github.com/cisco-grpc-connection-libs/ios-xr-grpc-python',
      author='Karthik Kumaravel',
      authoer_email='srirudrankumaravel@gmail.com',
      licencse='Apache 2.0',
      packages=['iosxr_grpc'],
      install_requires=[
          'grpcio==1.0.0',
      ],
      zip_safe=False)
