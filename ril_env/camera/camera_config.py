from dataclasses import dataclass


@dataclass
class CameraConfig:
    """
    :config_param internal_serial: refers to the serial number for the camera
                                   attached to the arm
    :config_param external_serial: refers to the serial number for the camera
                                   not attached to the arm
    :config_param overlay_alpha: higher means overlay recorded frames
                                 become more prominent

    This needs to be updated/added to, there are a lot more parameters we can change.
    """

    internal_serial: str = "317222072157"
    external_serial: str = "317422075456"
    external_2_serial: str = "317422074281"

    overlay_alpha: float = 0.4
