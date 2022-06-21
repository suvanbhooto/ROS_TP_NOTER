def _init_markers(self):
        self.marker_idx = 0
        self.marker_array_msg = MarkerArray()
        for i in range(self.max_markers):
            marker = Marker()
            marker.header.frame_id = self.global_frame
            marker.id = self.marker_idx
            marker.type = 2
            marker.action = 2
            marker.pose = Pose()
            marker.color.r = 0.0
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker.color.a = 0.0
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
            marker.frame_locked = False
            marker.ns = "Goal-%u"%i
            self.marker_array_msg.markers.append(marker) 
