import pathlib

from mythic_container.C2ProfileBase import C2Profile, C2ProfileParameter, ParameterType
import mythic_container.mythic_service


class notion(C2Profile):
    name = "notion"
    description = (
        "C2 channel using Notion as a covert transport. "
        "Leverages the Notion API to store tasks and results in a shared database, "
        "blending into legitimate SaaS traffic (Living off Trusted Sites)."
    )
    author = "@bbuddha"
    is_p2p_c2 = False
    is_server_routed = True
    mythic_encrypts = True

    server_folder_path = pathlib.Path(__file__).parent.parent.parent / "c2_code"
    server_binary_path = server_folder_path / "main.py"

    parameters = [
        C2ProfileParameter(
            name="integration_token",
            description="Notion Integration Token (starts with 'ntn_...' or 'secret_...')",
            default_value="",
            parameter_type=ParameterType.String,
            required=True,
        ),
        C2ProfileParameter(
            name="database_id",
            description=(
                "ID of the Notion database used as C2 channel. "
                "The integration must have access to this database."
            ),
            default_value="",
            parameter_type=ParameterType.String,
            required=True,
        ),
        C2ProfileParameter(
            name="callback_interval",
            description="Agent polling interval in seconds",
            default_value="10",
            parameter_type=ParameterType.Number,
            required=False,
        ),
        C2ProfileParameter(
            name="callback_jitter",
            description="Jitter percentage applied to polling interval (0-50)",
            default_value="10",
            parameter_type=ParameterType.Number,
            required=False,
        ),
    ]


mythic_container.mythic_service.start_and_run_forever()
