from stdimage import StdImageField

class MyStdImageField(StdImageField):

    @classmethod
    def process_variation(cls, variation, image):
        """Process variation before actual saving."""
        save_kargs = {}
        file_format = image.format
        save_kargs['format'] = file_format

        resample = variation['resample']

        if cls.is_smaller(image, variation):
            factor = 1
            while image.size[0] / factor \
                    > 2 * variation['width'] \
                    and image.size[1] * 2 / factor \
                    > 2 * variation['height']:
                factor *= 2
            if factor > 1:
                image.thumbnail(
                    (int(image.size[0] / factor),
                    int(image.size[1] / factor)),
                    resample=resample
                )

            size = variation['width'], variation['height']
            size = tuple(int(i) if i is not None else i
                        for i in size)

            if file_format == 'JPEG':
                # http://stackoverflow.com/a/21669827
                image = image.convert('RGB')
                save_kargs['optimize'] = True
                save_kargs['quality'] = 'web_very_high'
                if size[0] * size[1] > 10000:  # roughly <10kb
                    save_kargs['progressive'] = True

            if variation['crop']:
                image = ImageOps.fit(
                    image,
                    size,
                    method=resample
                )
            else:
                image.thumbnail(
                    size,
                    resample=resample
                )

        return image, save_kargs