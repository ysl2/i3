import i3ipc


def main():
    ipc = i3ipc.Connection()
    focused = ipc.get_tree().find_focused()

    if focused.window_class == 'wpsoffice':
        focused.command('exec --no-startup-id killall wps wpsoffice wpscloudsvr')
        return
    focused.command('kill')


if __name__ == '__main__':
    main()
