from __future__ import annotations


class Resolution:
    def __init__(self, width: int = 1920, height: int = 1080) -> None:
        self.height = height
        self.width = width

    def get_resolution(self):
        return (self.width, self.height)

    @staticmethod
    def resolution_factory(req: str) -> Resolution:
        mappings = {
            "240p": Resolution(426, 240),
            "360p": Resolution(640, 360),
            "480p": Resolution(854, 480),
            "sd": Resolution(854, 480),
            "720p": Resolution(1280, 720),
            "hd": Resolution(1280, 720),
            "1080p": Resolution(1920, 1080),
            "fhd": Resolution(1920, 1080),
            "1440p": Resolution(2560, 1440),
            "2k": Resolution(2560, 1440),
            "2160p": Resolution(3840, 2160),
            "4k": Resolution(3840, 2160),
        }
        if req in mappings:
            return mappings[req]
        raise ValueError("Invalid resolution request")
