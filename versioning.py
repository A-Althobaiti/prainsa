import os

def update_version(current_version):
	current_version = [int(i) for i in current_version.split('.')]

	if current_version[0] == 9 and current_version[1] == 9 and current_version[2] == 9:
		raise Exception('The maximum versioning exceeded')

	updated_version = current_version[0] * 100 + current_version[1] * 10 + current_version[2] + 1
	updated_version = '.'.join(str(updated_version).zfill(3))

	with open('./version', 'w') as fd:
		fd.write(updated_version)

	return updated_version


def get_version():
	if not os.path.isfile('./version'):
		with open('./version', 'w') as fd:
			fd.write('0.0.1')
		return '0.0.1'

	current_version = None
	with open('./version') as fd:
		current_version = fd.read(5)

	return update_version(current_version)
