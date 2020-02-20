import request from "@/utils/request"

export function fetchRegions() {
  return request({
    url: "/regions",
    method: "get"
  })
}

export function fetchFBUsers() {
  return request({
    url: "/facebook-users",
    method: "get"
  })
}

