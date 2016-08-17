# Project Name

Some scripts to help update an old version of project translation

## Requirements
pip install polib

## Usage

- Checkout the old version of the project
- Check how much is untranslated using untranslated.py -p <POT FILE NAME>
- Download latest translated .po files from the latest branch or from the translation vendor -p <POT FILE NAME>
- Update currant po files from the latest one using update.py -b <OLD/BASE POT FILE> -u <UPDATED POT FILE>
- Generate new mo files using potomo.py -p <POT FILE NAME> -m <MO FILE NAME>

### example

To update translation of https://github.com/Edraak/edx-ora2/tree/edraak/0.2.4

- Downloaded openassessment-js_ar.po openassessment_ar.po from https://www.transifex.com/open-edx/edx-platform/language/ar/
- Found out the arabic base po file is out of dates.
- Copied the english django.po djangojs.po to ar folder
- Excuted: 
```
python update.py -b django.po olddjango.po 
python update.py -b django.po -u openassessment_ar.po 
python update.py -b djangojs.po -u olddjangojs.po 
python update.py -b djangojs.po -u openassessment-js_ar.po 

```
- Manually added missing 10 translations
- Excuted:
```
python potomo.py -p django.po -m django.mo 
python potomo.py -p djangojs.po -m djangojs.mo 
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D