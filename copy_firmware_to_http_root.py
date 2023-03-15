Import("env")
board = env.BoardConfig()
mcu = board.get("build.mcu", "esp32")
env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(" ".join([
        '"$PYTHONEXE" "$OBJCOPY"',
        "--chip", mcu, "elf2image",
        "--flash_mode", "${__get_board_flash_mode(__env__)}",
        "--flash_freq", "${__get_board_f_flash(__env__)}",
        "--flash_size", board.get("upload.flash_size", "4MB"),
        "-o", "$PROJECT_DIR/http_server_root/hello-world.bin", "$BUILD_DIR/${PROGNAME}.elf"
    ]), "Building $PROJECT_DIR/http_server_root/hello-world.bin")
)