from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star


class EchoPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("echo")
    async def echo(self, event: AstrMessageEvent):
        """原样返回用户文字消息链."""
        
        # 返回 `/echo` 之后的文字内容
        remainder = event.message_str[len("/echo"):].lstrip()

        if remainder:
            yield event.plain_result(remainder)
        else:
            yield event.plain_result("PONG")
