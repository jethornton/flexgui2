
def jog(parent, action, axis=None, direction=None):
	print('jog')
	vel = parent.jog_vel_sl.value() / 60
	if action:
		print(f'action {action} axis {axis} direction {direction}')
	else:
		print(f'action {action}')

