Import("env")
import shutil
from pathlib import Path

def post_program_action(source, target, env):
    print("Copying program to http root")
    program_path = target[0].get_abspath()
    print("Program path", program_path)
    target_path = Path(env.subst("$PROJECT_DIR")) / "http_server_root" / "hello-world.bin"
    shutil.copy(src=program_path, dst=target_path)

env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", post_program_action)