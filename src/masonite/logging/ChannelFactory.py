from .channels import SingleChannel, DailyChannel, SlackChannel, StackChannel, SyslogChannel, TerminalChannel

class ChannelFactory:

    channels = {
        'single': SingleChannel,
        'daily': DailyChannel,
        'slack': SlackChannel,
        'stack': StackChannel,
        'syslog': SyslogChannel,
        'terminal': TerminalChannel
    }

    @classmethod
    def make(cls, channel):
        return cls.channels.get(channel)