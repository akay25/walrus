import request from "@/utils/request"

export function fetchLinkTypes() {
  return request({
    url: "/link-types",
    method: "get"
  })
}

export function fetchLinks() {
  return request({
    url: "/facebook-links",
    method: "get"
  })
}

export function reloadLinks() {
  return request({
    url: "/reload-links",
    method: "get"
  })
}

