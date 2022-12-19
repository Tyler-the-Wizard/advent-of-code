input = require(game.ServerScriptService.Input)

lava = Instance.new('Folder', workspace)
lava.Name = 'Lava'
filler = Instance.new('Folder', workspace)
filler.Name = 'Filler'

function get_adj_pos(x, y, z)
	return {
		{x+1, y, z},
		{x-1, y, z},
		{x, y+1, z},
		{x, y-1, z},
		{x, y, z+1},
		{x, y, z-1}
	}
end

function calc_surface_area(folder)
	local surface_area = 0
	for _, part in pairs(folder:GetChildren()) do
		local this_pos = {
			part.Position.X,
			part.Position.Y,
			part.Position.Z
		}
		for _, pos in pairs(get_adj_pos(unpack(this_pos))) do
			if not folder_intersects_point(folder, Vector3.new(unpack(pos))) then
				surface_area = surface_area + 1
			end
		end
	end
	
	return surface_area
end

-- https://devforum.roblox.com/t/_/582652/5
local function part_intersects_point(part, point)
	local delta = part.CFrame:pointToObjectSpace(point)
	delta = Vector3.new(math.abs(delta.X), math.abs(delta.Y), math.abs(delta.Z))
	local halfSize = part.Size / 2

	return delta.X <= halfSize.X
	   and delta.Y <= halfSize.Y
	   and delta.Z <= halfSize.Z
end

function folder_intersects_point(folder, point)
	for _, part in pairs(folder:GetChildren()) do
		if part_intersects_point(part, point) then
			return true
		end
	end
	
	-- dodge roblox execution timeout lol
	if math.random(1, 100) == 1 then
		wait()
	end
	
	return false
end

-- Create the lava cubes
p0 = Instance.new('Part')
p0.BrickColor = BrickColor.new('Really red')
p0.Material = 'CrackedLava'
p0.Anchored = true
p0.Size = Vector3.new(.8,.8,.8)

for i, pos in pairs(input) do
	local p = p0:Clone()
	p.CFrame = CFrame.new(
		pos[1], pos[2] + 10, pos[3]
	)
	p.Parent = lava
	p.Name = '(' ..
		tostring(pos[1]) .. ',' ..
		tostring(pos[2]) .. ',' ..
		tostring(pos[3]) .. ')'
	
	if i % 10 == 0 then
		wait()
	end
end

lava_surface_area = calc_surface_area(lava)
print('Total surface area: ' .. lava_surface_area)

wait(2)

--for _, p in pairs(lava:GetChildren()) do
--	p.Material = 'SmoothPlastic'
--	delay(0, function()
--		for t = 0, 0.8, 0.05 do
--			p.Transparency = t
--			wait()
--		end
--	end)
--end

--wait(3)

-- Create the filler cubes
p0.BrickColor = BrickColor.new('Lime green')
p0.Material = 'SmoothPlastic'

i = 1
function recursive_fill(x, y, z)
	local p = p0:Clone()
	p.CFrame = CFrame.new(x, y, z)
	p.Parent = filler
	
	for _, pos in pairs(get_adj_pos(x, y, z)) do
		if not (
			folder_intersects_point(lava, Vector3.new(unpack(pos))) or
			folder_intersects_point(filler, Vector3.new(unpack(pos)))
		) then
			recursive_fill(unpack(pos))
		end
	end
	
	i = i + 1
	if i % 10 == 0 then
		wait()
	end
end

recursive_fill(10, 20, 10)

interior_surface_area = calc_surface_area(filler)
print('Exterior surface area: ' .. lava_surface_area - interior_surface_area)
