
import xml.etree.ElementTree as XML


def github_pull_request_status(parser, xml_parent, data):
    """yaml: github-pull-request-status
    Requires the Jenkins :jenkins-wiki:`GitHub Pull Request Builder Plugin
    <GitHub+pull+request+builder+plugin>`.

    This is intended to follow the github-pull-request trigger as it
    extends it with new functionality

    Example::

      trigger:
        - github-pull-request:
        - github-pull-request-status:
            commit-status-context: default
            status-url: "http://example.com/my-public-test-check/"
            triggered-status: Build triggered.
            started-status: Build started.
    """
    if data is None:
        data = {}

    ghprb = xml_parent.find('org.jenkinsci.plugins.ghprb.'
                            'GhprbTrigger')
    if ghprb is None:
        raise ValueError('github-pull-request trigger must be set before '
                         'github-pull-request-status')
    extensions = ghprb.find('extensions')
    if extensions is None:
        extensions = XML.SubElement(ghprb, 'extensions')
    status = XML.SubElement(extensions, 'org.jenkinsci.plugins.ghprb.'
                                        'extensions.status.GhprbSimpleStatus')
    for prop_name, node_name in (('commit-status-context', 'commitStatusContext'),
                                 ('status-url', 'statusUrl'),
                                 ('triggered-status', 'triggeredStatus'),
                                 ('started-status', 'startedStatus')):
        if prop_name in data:
            XML.SubElement(status, node_name).text = data[prop_name]
