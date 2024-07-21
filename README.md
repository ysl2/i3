# ![Logo](logo-30.png) i3

![](i3wm.png)

Build i3 and i3blocks from official source repo.

```bash
git clone git@github.com:ysl2/i3.git ~/.config/i3
```

Also:

```bash
pip install autotiling
cargo install i3-autolayout
sudo apt install xdotool rofi xcwd yad

# If using anaconda, you should `conda install -c conda-forge libstdcxx-ng`
# Ref: https://stackoverflow.com/a/75333466/13379393
# Disable this due to bug.
# git clone git@github.com/ysl2/i3expod-ng.git && cd i3expod-ng && make install
```

`config_bak` and `i3blocs.bak.conf` are the official config files, just for backup.

Log dir: `~/.vocal/.lock/i3`
