"""Small, generated Pillow icons for dashboard cards."""

import math

from PIL import Image, ImageDraw, ImageFont, ImageTk


class IconFactory:
    """Create and cache compact Pillow icons for dashboard and navigation."""

    def __init__(self):
        self._cache = {}

    def create(self, symbol, size=34, color="#197A55"):
        key = (symbol, size, color)
        if key not in self._cache:
            image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.ellipse((1, 1, size - 2, size - 2), fill=color)
            font = ImageFont.load_default(size=max(12, size // 2))
            bounds = draw.textbbox((0, 0), symbol, font=font)
            x = (size - (bounds[2] - bounds[0])) / 2 - bounds[0]
            y = (size - (bounds[3] - bounds[1])) / 2 - bounds[1]
            draw.text((x, y), symbol, font=font, fill="white")
            self._cache[key] = ImageTk.PhotoImage(image)
        return self._cache[key]

    def navigation(self, page, size=24):
        """Draw a small, category-related icon for each sidebar destination."""
        key = ("navigation", page, size)
        if key in self._cache:
            return self._cache[key]

        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        fill = "#E5F5EA"
        accent = "#9ED9B3"
        line_width = max(2, size // 12)
        center = size // 2
        inset = size // 5

        if page == "Dashboard":
            gap = size // 9
            box = (size - 2 * inset - gap) // 2
            for row in range(2):
                for column in range(2):
                    x = inset + column * (box + gap)
                    y = inset + row * (box + gap)
                    draw.rounded_rectangle(
                        (x, y, x + box, y + box), radius=3,
                        fill=fill if row + column != 2 else accent,
                    )
        elif page in ("WaterTracker", "Water"):
            draw.polygon(
                [
                    (center, inset - 1), (size - inset, center - 1),
                    (center + 1, size - inset), (inset, center - 1),
                ],
                fill=fill,
            )
            draw.ellipse(
                (center - size // 10, center + size // 7,
                 center + size // 10, center + size // 3),
                fill=accent,
            )
        elif page == "Medicine":
            capsule = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            capsule_draw = ImageDraw.Draw(capsule)
            capsule_draw.rounded_rectangle(
                (size * .14, size * .32, size * .86, size * .68),
                radius=size // 5, fill=fill, outline=accent, width=line_width,
            )
            capsule_draw.line(
                (size * .5, size * .34, size * .5, size * .66),
                fill="#197A55", width=line_width,
            )
            image = capsule.rotate(-40, resample=Image.Resampling.BICUBIC)
        elif page == "Exercise":
            draw.ellipse(
                (center - 3, inset, center + 3, inset + 6), fill=fill
            )
            draw.line((center, inset + 7, center, size - inset), fill=fill, width=line_width)
            draw.line(
                (center, center, inset, center - 2),
                fill=accent, width=line_width,
            )
            draw.line(
                (center, center, size - inset, center - 3),
                fill=accent, width=line_width,
            )
            draw.line(
                (center, size - inset, inset, size - inset + 2),
                fill=fill, width=line_width,
            )
            draw.line(
                (center, size - inset, size - inset, size - inset + 2),
                fill=fill, width=line_width,
            )
        elif page == "Meditation":
            draw.ellipse(
                (center - size * .1, inset, center + size * .1, size * .72),
                fill=fill, outline=accent, width=1,
            )
            draw.polygon(
                [(center, size * .78), (size * .12, size * .43),
                 (size * .27, size * .32), (center, size * .78)],
                fill=accent,
            )
            draw.polygon(
                [(center, size * .78), (size * .73, size * .32),
                 (size * .88, size * .43), (center, size * .78)],
                fill=accent,
            )
            draw.arc(
                (size * .18, size * .54, size * .82, size * .94),
                start=0, end=180, fill=fill, width=line_width,
            )
        elif page == "Custom":
            draw.line(
                (inset, size - inset, size - inset, inset),
                fill=fill, width=line_width + 1,
            )
            draw.polygon(
                [(size - inset, inset), (size - inset - 1, inset + 6),
                 (size - inset - 6, inset + 1)],
                fill=accent,
            )
        elif page == "Manage":
            for row in range(3):
                y = inset + row * (size - 2 * inset) // 2
                draw.rounded_rectangle(
                    (inset, y, inset + 4, y + 4), radius=1, fill=accent
                )
                draw.line(
                    (inset + 7, y + 2, size - inset, y + 2),
                    fill=fill, width=line_width,
                )
        elif page == "History":
            draw.ellipse(
                (inset, inset, size - inset, size - inset),
                outline=fill, width=line_width,
            )
            draw.line(
                (center, center, center, inset + 3),
                fill=accent, width=line_width,
            )
            draw.line(
                (center, center, size - inset - 3, center + 2),
                fill=accent, width=line_width,
            )
        elif page == "Report":
            baseline = size - inset
            for index, height in enumerate((size * .28, size * .48, size * .68)):
                x = inset + index * (size - 2 * inset) // 3
                draw.rounded_rectangle(
                    (x, baseline - height, x + size // 6, baseline),
                    radius=2, fill=accent if index == 1 else fill,
                )
        elif page == "Calendar":
            draw.rounded_rectangle(
                (inset, inset + 3, size - inset, size - inset),
                radius=3, outline=fill, width=line_width,
            )
            draw.line(
                (inset, inset + 8, size - inset, inset + 8),
                fill=accent, width=line_width,
            )
            for x in (inset + 5, center, size - inset - 5):
                draw.ellipse((x - 1, center + 1, x + 1, center + 3), fill=fill)
        elif page == "Achievements":
            draw.polygon(
                [(center, inset), (center + 3, center - 2),
                 (size - inset, center), (center + 4, center + 3),
                 (center + 5, size - inset), (center, center + 5),
                 (center - 5, size - inset), (center - 4, center + 3),
                 (inset, center), (center - 3, center - 2)],
                fill=accent,
            )
        elif page == "Profile":
            draw.ellipse(
                (center - 4, inset, center + 4, inset + 8), fill=fill
            )
            draw.ellipse(
                (inset, center, size - inset, size - inset + 3),
                fill=accent,
            )
        elif page == "Settings":
            draw.ellipse(
                (inset, inset, size - inset, size - inset),
                outline=fill, width=line_width + 1,
            )
            draw.ellipse(
                (center - 3, center - 3, center + 3, center + 3),
                fill=accent,
            )
            for angle in range(0, 360, 45):
                radians = math.radians(angle)
                inner = size * .34
                outer = size * .46
                draw.line(
                    (
                        center + inner * math.cos(radians),
                        center + inner * math.sin(radians),
                        center + outer * math.cos(radians),
                        center + outer * math.sin(radians),
                    ),
                    fill=fill, width=line_width,
                )

        self._cache[key] = ImageTk.PhotoImage(image)
        return self._cache[key]
