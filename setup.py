#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-coref-plugin-pronomial=ovos_coref_plugin_pronomial:PronomialCoreferenceSolver'
setup(
    name='ovos-coref-plugin-pronomial',
    version='0.0.1',
    description='A coreference resolution plugin for mycroft',
    url='https://github.com/OpenVoiceOS/ovos-coref-plugin-pronomial',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_coref_plugin_pronomial'],
    install_requires=["ovos-plugin-manager", "pronomial"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'intentbox.coreference': PLUGIN_ENTRY_POINT}
)
