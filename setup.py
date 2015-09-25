from setuptools import setup

setup(
    name='jenkins-jobs-github-pr-status',
    version='1.0.1',
    description='Jenkins Job Builder Github PR Status',
    url='https://github.com/Alphadelta14/jenkins-jobs-github-pr-status',
    author='Alphadelta14',
    author_email='alpha@projectpokemon.org',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.triggers': [
            'github-pull-request-status = jenkins_jobs_github_pr_status.github_pr_status:github_pull_request_status']},
    packages=['jenkins_jobs_github_pr_status'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])