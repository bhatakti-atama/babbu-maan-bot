from PIL import Image, ImageDraw, ImageFont, ImageSequence
import io

def AddTextToImage(image_bytes, text, position="bottom", font_size=20):
    img = Image.open(io.BytesIO(image_bytes))
    frames = []
    font = ImageFont.truetype("fonts/impact.ttf", font_size)

    is_animated = getattr(img, "is_animated", False)

    def draw_text(frame):
        frame = frame.convert("RGBA")
        txt_layer = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (frame.width - text_width) // 2
        y = 10 if position == "top" else frame.height - text_height - 10

        draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))
        return Image.alpha_composite(frame, txt_layer)

    if is_animated:
        for frame in ImageSequence.Iterator(img):
            edited = draw_text(frame)
            frames.append(edited.convert("P"))
    else:
        edited = draw_text(img)
        output = io.BytesIO()
        edited.convert("RGB").save(output, format="PNG")
        output.seek(0)
        return output

    # For GIF output
    output = io.BytesIO()
    frames[0].save(output, format="GIF", save_all=True,
                   append_images=frames[1:],
                   duration=img.info.get("duration", 100),
                   loop=img.info.get("loop", 0))
    output.seek(0)
    return output