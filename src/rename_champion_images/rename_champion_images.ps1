# champion_images 폴더에 있는 파일 이름에서 ' OriginalSquare'를 제거
Get-ChildItem -Path "../champion_images" -Filter "*OriginalSquare.png" | Rename-Item -NewName { $_.Name -replace ' OriginalSquare', '' }
