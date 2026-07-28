# ARGO Troubleshooting

## Compatibility

Published wiki requirements:
- Windows XP or newer;
- .NET Framework 4;
- Excel 2007–2016, 32/64-bit.

The repository is archived and says ARGO is no longer actively developed. Treat later Excel/Windows versions as unverified unless tested.

## Add-in disabled

In Excel:
1. File → Options → Add-ins.
2. Manage: Disabled Items.
3. Enable ARGO.

## Application add-ins disabled

Excel:
1. File → Options → Trust Center.
2. Trust Center Settings → Add-ins.
3. Ensure "Disable all Application Add-ins" is not checked.

## StatLib3 or dependency loading failure

Known wiki causes:
- launching the `.xll` from inside a ZIP;
- moving the `.xll` away from supporting files;
- downloaded files blocked by Windows policy.

Keep the ARGO `.xll` in the folder with its DLL dependencies. Extract the ZIP/setup files first. Unblock downloaded files where permitted by organisational policy.

## Missing ARGO tab

Check:
- correct 32/64-bit ARGO build;
- add-in enabled;
- files extracted;
- dependencies co-located;
- Windows blocked-file status;
- Excel trust settings;
- old version unchecked before loading another version.

## Formula errors

### `#NAME?`
Likely:
- ARGO add-in not loaded;
- wrong function name;
- smart quotes or corrupted text;
- formula generated in an environment without ARGO.

### `#VALUE!`
Likely:
- invalid parameter domain;
- wrong order;
- malformed optional arguments;
- invalid lower/upper bound;
- wrong Excel separator.

### Formula shown as text
Check:
- cell format set to Text;
- leading apostrophe;
- calculation mode;
- formula begins with `=`.

## Mac

Do not troubleshoot ARGO as though it were a native Mac add-in. The published package is a Windows Excel XLL/COM-style add-in. A Windows VM or Windows machine may be required.
