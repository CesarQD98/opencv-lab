import cv2
import time
import datetime

VIDEO_SOURCE = 0
PRIMARY_FONT = cv2.FONT_HERSHEY_PLAIN
PRIMARY_FONT_SCALE = 1.5
PRIMARY_FONT_THICKNESS = 2
BACKGROUND_RECTANGLE_COLOR = (0, 0, 0)
BACKGROUND_RECTANGLE_OFFSET = 5


def customPutText(
    image,
    text: str,
    pivot_point: tuple[int, int],
    font_type=cv2.FONT_HERSHEY_DUPLEX,
    font_scale: int = 1,
    text_color: tuple[int, int, int] = (255, 255, 255),
    text_thickness: int = 1,
    background_offset: int = 5,
    background_color: tuple[int, int, int] = (0, 0, 0),
):
    # pivot_point is the top-left corner of the custom text box
    (text_width, text_height), _ = cv2.getTextSize(
        text, font_type, font_scale, text_thickness
    )

    cv2.rectangle(
        image,
        (
            pivot_point[0] - background_offset,
            pivot_point[1] + background_offset,
        ),
        (
            pivot_point[0] + text_width + background_offset,
            pivot_point[1] - text_height - background_offset,
        ),
        background_color,
        cv2.FILLED,
    )
    cv2.putText(
        image, text, pivot_point, font_type, font_scale, text_color, text_thickness
    )


def main():
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    (width, height) = (
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
    )

    while True:
        _, frame = cap.read()

        current_time_text = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")

        customPutText(
            image=frame,
            font_type=PRIMARY_FONT,
            font_scale=PRIMARY_FONT_SCALE,
            text_thickness=PRIMARY_FONT_THICKNESS,
            text=current_time_text,
            pivot_point=(0, height - 10),
            background_color=BACKGROUND_RECTANGLE_COLOR,
        )

        customPutText(
            frame,
            text="Sample text",
            font_type=PRIMARY_FONT,
            font_scale=PRIMARY_FONT_SCALE,
            text_thickness=PRIMARY_FONT_THICKNESS,
            pivot_point=(0, height // 2),
        )

        cv2.imshow(
            "Webcam feed",
            frame,
        )

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
