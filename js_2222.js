!function (e, t, r) {
    var n = {
        ie: !!("ActiveXObject" in e && /(msie |Trident\/.*rv:)(\d*)/i.test(navigator.userAgent)) && RegExp.$2,
        firefox: /Firefox/i.test(navigator.userAgent),
        init: function () {
            var e = navigator.userAgent;
            n.browser = function () {
                var t = "";
                return t = n.ie ? "ie" + n.ie : /Chrome/i.test(e) ? "chrome" : /Opera/i.test(e) ? "opera" : /FireFox/i.test(e) ? "firefox" : "other"
            }(), n.system = function () {
                var t = "";
                return t = /Windows NT 10.0/.test(e) ? "windows 10" : /Windows NT 5.1/.test(e) ? "windows xp" : /Windows NT 6.1/.test(e) ? "windows 7" : /Windows NT 6.2/.test(e) ? "windows 8" : /Windows NT 6.0/.test(e) ? "windows vista" : /Windows NT 5.2/.test(e) ? "windows 2003" : /Mac OS/.test(e) ? "mac" : /Linux/.test(e) ? "linux" : "other"
            }()
        }
    }, a = {
        domain: function () {
            return "yy.duowan.com" == e.location.hostname ? "//yy.duowan.com" : "//www.yy.com"
        }(), UA: n, formator: function (e) {
            return parseInt(e, 10).toLocaleString(r, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).replace(/\.00$/, "") || 0
        }, dateFormator: function (e, t) {
            function r(e) {
                return e.toString().length < 2 ? "0" + e : e
            }

            return t.replace(/%([a-zA-Z])/g, function (t, n) {
                switch (n) {
                    case"Y":
                        return e.getFullYear();
                    case"M":
                        return r(e.getMonth() + 1);
                    case"d":
                        return r(e.getDate());
                    case"H":
                        return r(e.getHours());
                    case"m":
                        return r(e.getMinutes());
                    case"s":
                        return r(e.getSeconds());
                    default:
                        throw new Error("Unsupported format code: " + n)
                }
            })
        }, isPropTruthy: function (e) {
            return function (t) {
                return t[e]
            }
        }, transfromPropName: function (e, t) {
            return function (r) {
                if (r[e]) {
                    var n = Object.assign({}, r);
                    return n[t] = n[e], delete n[e], n
                }
            }
        }, escape: function (e) {
            var t = {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;",
                "/": "&#x2F;",
                "`": "&#x60;",
                "=": "&#x3D;"
            };
            return String(e).replace(/[&<>"'`=\/]/g, function (e) {
                return t[e]
            })
        }, escapeToNull: function (e) {
            return String(e).replace(/[<>"'`?\/]/g, "")
        }, isElementAppearInParentView: function (t, r) {
            r = r || e;
            var n = {
                    top: 0,
                    right: e.innerWidth,
                    bottom: e.innerHeight,
                    left: 0,
                    height: e.innerHeight,
                    width: e.innerWidth
                }, o = a.getRelativeRect(t, r), i = r === e ? n : r.getBoundingClientRect(),
                s = i.height || i.bottom - i.top, l = parent.width || i.right - i.left;
            return o.top <= s && o.left <= l
        }, getRectWidth: function (e) {
            var t = e.getBoundingClientRect();
            return t.width || t.right - t.left
        }, getRelativeRect: function (t, r) {
            r = r || e;
            var n = {
                top: 0,
                right: e.innerWidth,
                bottom: e.innerHeight,
                left: 0,
                height: e.innerHeight,
                width: e.innerWidth
            }, a = t.getBoundingClientRect(), o = r === e ? n : r.getBoundingClientRect();
            return {top: a.top - o.top, right: a.right - o.right, bottom: a.bottom - o.bottom, left: a.left - o.left}
        }, unsign: function (e) {
            return e < 0 ? 0 : e
        }, filterByProperty: function (e, t, r) {
            return e.filter(function (e) {
                return e[t] === r
            })
        }, activateLazyImage: function (t, r) {
            var n = {
                placeholder: "", failure_limit: 1 / 0, load: function () {
                    $(this).css("visibility", "visible")
                }
            };
            t = $.extend({}, n, t), $(".lazy").lazyload(t), r || $(e).trigger("resize")
        }, scrollTo: function (e, t) {
            return t = "undefined" != typeof t ? t : 400, new Promise(function (r) {
                $("html, body").stop().animate({scrollTop: $(e).offset().top - $(".w-head__main").height()}, t, r)
            })
        }, scrollTop: function (e) {
            return e = "undefined" != typeof e ? e : 400, new Promise(function (t) {
                $("html, body").stop().animate({scrollTop: 0}, e, t)
            })
        }, injectCSS: function (e, t) {
            t && $('<style id="' + e + '" type="text/css">' + t + "</style>").appendTo("head")
        }, replaceCSS: function (e, t) {
            t && ($("#" + e).remove(), a.injectCSS(e, t))
        }, touchCSS: function (e, r) {
            var n = t.getElementById(e);
            return n ? void a.replaceCSS(e, r) : void a.injectCSS(e, r)
        }, getParameterByName: function (t, r) {
            r || (r = e.location.href), t = t.replace(/[[\]]/g, "\\$&");
            var n = new RegExp("[?&]" + t + "(=([^&#]*)|&|#|$)"), a = n.exec(r);
            return a ? a[2] ? decodeURIComponent(a[2].replace(/\+/g, " ")) : "" : null
        }, fill: function (e, t, n, a) {
            if (!Array.isArray(e)) throw new TypeError("array is not a Array");
            var o = e.length;
            n = parseInt(n, 10) || 0, a = a === r ? o : parseInt(a, 10) || 0;
            var i, s;
            for (i = n < 0 ? Math.max(o + n, 0) : Math.min(n, o), s = a < 0 ? Math.max(o + a, 0) : Math.min(a, o); i < s; i++) e[i] = t;
            return e
        }, arrayPad: function (e, t, r) {
            return e.length >= t ? e : [].concat(e, a.fill(Array(t), r).slice(0, t - e.length))
        }, flash: {
            init: function (e, t) {
                var r = {
                    wmode: "opaque",
                    width: 300,
                    height: 300,
                    flashvars: "",
                    flashUrl: "",
                    fullscreen: !1,
                    bgcolor: "#000000"
                };
                if ("object" == typeof t) {
                    if ("undefined" != typeof t.wmode) {
                        switch (t.wmode.toLowerCase()) {
                            case"opaque":
                                r.wmode = "opaque";
                                break;
                            case"window":
                                r.wmode = "window";
                                break;
                            case"transparent":
                                r.wmode = "transparent"
                        }
                        r.wmode = t.wmode
                    }
                    "undefined" != typeof t.width && (r.width = t.width), "undefined" != typeof t.height && (r.height = t.height), "undefined" != typeof t.flashvars && (r.flashvars = t.flashvars), "undefined" != typeof t.flashUrl && (r.flashUrl = t.flashUrl), "undefined" != typeof t.fullscreen && (r.fullscreen = t.fullscreen), "undefined" != typeof t.bgcolor && (r.bgcolor = t.bgcolor)
                }
                if ("" !== r.flashUrl) {
                    var n = ['<object id="{$name}" name="{$name}" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=10.0.32" data="{$flashUrl}" width="{$width}" height="{$height}">', '<param name="movie" value="{$flashUrl}" />', '<param name="flashvars" value="{$flashvars}" />', '<param name="quality" value="high" />', '<param name="allowScriptAccess" value="always" />', '<param name="wmode" value="{$wmode}"/>', '<param name="bgcolor" value="{$bgcolor}"/>', '<param name="allowFullScreen" value="{$fullscreen}"/>', '<param name="allowFullScreenInteractive" value="{$fullscreen}"/>', '<embed id="embed_{$name}" name="{$name}" src="{$flashUrl}" width="{$width}" allowFullScreen="{$fullscreen}" allowFullScreenInteractive="{$fullscreen}" height="{$height}" allowScriptAccess="always" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" flashvars="{$flashvars}" type="application/x-shockwave-flash" wmode="{$wmode}" bgcolor="{$bgcolor}"></embed>', "</object>"].join("");
                    return n.replace(/\{if ie\}(.*?)\{endif ie\}/g, ~navigator.appName.indexOf("Microsoft") ? "$1" : "").replace(/\{\$name\}/g, e).replace(/\{\$width\}/g, r.width).replace(/\{\$height\}/g, r.height).replace(/\{\$flashUrl\}/g, r.flashUrl).replace(/\{\$flashvars\}/g, r.flashvars).replace(/\{\$wmode\}/g, r.wmode).replace(/\{\$bgcolor\}/g, r.bgcolor).replace(/\{\$fullscreen\}/g, r.fullscreen)
                }
            }, write: function (e, r) {
                var n = this.init(e, r);
                n && t.write(n)
            }, add: function (e, t, r) {
                var n = this.init(t, r);
                e && n && (e.innerHTML = n)
            }, ctrl: function (e) {
                try {
                    var r = t.getElementById(e);
                    return a.UA.ie ? "object" == r.tagName.toLowerCase() ? r : "" : "embed" == r.tagName.toLowerCase() ? r : r.getElementsByTagName("embed")[0]
                } catch (n) {
                    console.warn(e)
                }
            }
        }, Promise: function (e) {
            var t = this;
            return t.queue = [], t.current = 0, t.isResolved = !1, t.then = function (e) {
                return "function" == typeof e && t.queue.push(e), t
            }, t.start = function () {
                var e = Array.prototype.slice.call(arguments);
                return t.resolve.apply(t, e), t
            }, t.resolve = function () {
                var e = Array.prototype.slice.call(arguments);
                e.push(t.resolve), t.current && e.push(t.queue[t.current - 1]), t.current != t.queue.length && t.queue[t.current++].apply(t, e)
            }, e && t.then(e), t
        }, type: function (e) {
            var t, r = Object.prototype.toString;
            return null === e ? t = String(e) : (t = r.call(e).toLowerCase(), t = t.substring(8, t.length - 1)), t
        }, isPlainObject: function (e) {
            var t, n = this, a = Object.prototype.hasOwnProperty;
            if (!e || "object" !== n.type(e)) return !1;
            if (e.constructor && !a.call(e, "constructor") && !a.call(e.constructor.prototype, "isPrototypeOf")) return !1;
            for (t in e) ;
            return t === r || a.call(e, t)
        }, extend: function () {
            var e, t, n, a, o, i, s = this, l = arguments[0] || {}, c = 1, u = arguments.length, h = !1;
            for ("boolean" == typeof l && (h = l, l = arguments[1] || {}, c = 2), "object" != typeof l && "function" !== s.type(l) && (l = {}), u === c && (l = this, --c); c < u; c++) if (null !== (e = arguments[c])) for (t in e) n = l[t], a = e[t], l !== a && (h && a && (s.isPlainObject(a) || (o = "array" === s.type(a))) ? (o ? (o = !1, i = n && "array" === s.type(n) ? n : []) : i = n && s.isPlainObject(n) ? n : {}, l[t] = s.extend(h, i, a)) : a !== r && (l[t] = a));
            return l
        }, reverseUnitFormat: function (e, t) {
            switch (t) {
                case 2:
                    return parseInt(e.split(",").join(""));
                default:
                    return e
            }
        }, unitFormat: function (e, t) {
            switch (e = parseFloat(e, 10), t) {
                case 1:
                    return e < 1e4 ? e : e < 1e8 ? Math.floor(e / 1e4 * 10) / 10 + "万" : Math.floor(e / 1e8 * 10) / 10 + "亿";
                case 2:
                    return parseInt(e, 10).toLocaleString().replace(/\.00$/, "") || 0;
                case 3:
                    return parseFloat(e, 10).toLocaleString().replace(/\.00$/, "") || 0;
                case"timeLength":
                    for (var r = Math.floor(e / 3600) + "", n = Math.floor((e - 3600 * r) / 60) + "", a = e - 3600 * r - 60 * n + ""; n.length < 2;) n = "0" + n;
                    for (; a.length < 2;) a = "0" + a;
                    for (; r.length < 2;) r = "0" + r;
                    return r + ":" + n + ":" + a;
                case 4:
                    return e < 1e4 ? e : e < 1e13 ? (e / 1e4).toFixed(1) + "万" : (e / 1e8).toFixed(1) + "亿";
                default:
                    return e
            }
        }, fromNow: function (e) {
            if (!e) return !1;
            var t = (new Date).getTime(), r = e, n = t - r, a = "", o = 6e4, i = 60 * o, s = 24 * i, l = 30 * s,
                c = 12 * l, u = n / c, h = n / l, f = n / (7 * s), p = n / s, d = n / i, m = n / o;
            return a = u >= 1 ? parseInt(u) + "年前" : h >= 1 ? parseInt(h) + "个月前" : f >= 1 ? parseInt(f) + "周前" : p >= 1 ? parseInt(p) + "天前" : d >= 1 ? parseInt(d) + "个小时前" : m >= 1 ? parseInt(m) + "分钟前" : "刚刚"
        }, getUrlParams: function () {
            var t = e.location.search;
            t = t.substr(1);
            var r = {};
            if ("" === t) return r;
            for (var n = t.split("&"), a = 0, o = n.length; a < o; a++) {
                var i = n[a], s = i.split("=");
                r[s[0]] = s[1]
            }
            return r
        }, thousandSeparator: function (e, t) {
            if (!e) return 0;
            var r;
            return t && t > 0 && (e = (+e).toFixed(t)), r = e.toString().split("."), r[0] = r[0].replace(/\B(?=(\d{3})+(?!\d))/g, ","), r.join(".")
        }, request: {
            search: function (e) {
                var t = location.search.replace(/[? ]/g, "");
                if ("" === t) return null;
                for (var r = t.split("&"), n = 0, a = r.length; n < a; n++) {
                    var o = r[n].split("=");
                    if (!(o.length <= 1)) {
                        var i = o[0], s = o[1];
                        if (i === e) return s
                    }
                }
                return null
            }, hash: function (t, r) {
                var n = location.hash.replace(/[# ]/g, ""), a = "undefined" != typeof r, o = !1;
                if ("" === n && !a) return null;
                for (var i = n.split("&"), s = 0, l = i.length; s < l; s++) {
                    var c = i[s].split("=");
                    if (!(c.length <= 1)) {
                        var u = c[0], h = c[1];
                        if (u === t) {
                            if (!a) return h;
                            i[s] = u + "=" + r, o = !0
                        }
                    }
                }
                return o || i.push(t + "=" + r), a ? (e.location.hash = i.join("&"), i.join("&")) : null
            }
        }, isFunction: function (e) {
            var t = {};
            return e && "[object Function]" === t.toString.call(e)
        }, eventRender: function (e, t, r) {
            if (e) {
                var n = e.getElementsByTagName("*"), a = function (e) {
                    var n = e.getAttribute("yy-el");
                    n && (t[n] = e, e.removeAttribute("yy-el"));
                    var a, o = e.getAttribute("yy-on"), i = function (t) {
                        var n = t.split(/\s*:\s*/g), a = n[0], o = r[n[1]];
                        n.length > 1 && o && ("undefined" != typeof $ ? $(e).on(a, o) : e.addEventListener ? e.addEventListener(a, o, !1) : e.attachEvent ? e.attachEvent("on" + a, function () {
                            o.call(e)
                        }) : e["on" + a] = o)
                    };
                    if (o) {
                        a = o.split(",");
                        for (var s = 0, l = a.length; s < l; s++) i(a[s]);
                        e.removeAttribute("yy-on")
                    }
                };
                a(e);
                for (var o = 0, i = n.length; o < i; o++) a(n[o])
            }
        }, isBelong: function (e, t) {
            for (var r = t; r; r = r.parentNode) if (r === e) return !0
        }, htmlEncode: function (e) {
            var t = {"<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "&": "&#38;"};
            return "string" != typeof e ? e : e.replace(/[<>"'&]/g, function (e) {
                return t[e]
            })
        }, htmlDecode: function (e) {
            var r = t.createElement("span");
            return r.innerHTML = e, r.innerText
        }, convertHttps: function (e) {
            if ("undefined" != typeof e) {
                var t = e.replace(/http:/g, ""), r = /^\/\/s[45]\.yy\.com/;
                return r.test(t) && (t = t.replace(r, "//s1.yy.com")), t
            }
            return e
        }, cookies: {
            get: function (r) {
                try {
                    var n = t.cookie.match(new RegExp("(^| )" + r + "=([^;]*)(;|$)"))
                } catch (a) {
                }
                return null !== n ? e.unescape(n[2]) : null
            }, set: function (r, n, a, o, i, s) {
                a || (a = 24);
                var l = new Date;
                l.setTime(l.getTime() + 60 * a * 60 * 1e3), t.cookie = r + "=" + e.escape(n) + ";expires=" + l.toGMTString() + (i ? ";domain=" + i : "") + (o ? ";path=" + o : "") + (s === !0 ? ";secure" : "")
            }, getWithDecode: function (r) {
                var n = t.cookie.match(new RegExp("(^| )" + r + "=([^;]*)(;|$)"));
                return null !== n ? e.decodeURI(n[2]) : null
            }, setWithEncode: function (r, n, a, o, i, s) {
                a || (a = 24);
                var l = new Date;
                l.setTime(l.getTime() + 60 * a * 60 * 1e3), t.cookie = r + "=" + e.encodeURI(n) + ";expires=" + l.toGMTString() + (i ? ";domain=" + i : "") + (o ? ";path=" + o : "") + (s === !0 ? ";secure" : "")
            }, del: function (e) {
                var r = new Date;
                r.setTime(r.getTime() - 6e4);
                var n = this.get(e);
                null !== n && (t.cookie = e + "=" + n + ";expires=" + r.toGMTString())
            }, erase: function (e, r, n) {
                a.cookies.get(e) && (t.cookie = e + "=" + (r ? ";path=" + r : "") + (n ? ";domain=" + n : "") + ";expires=Thu, 01 Jan 1970 00:00:01 GMT")
            }, keys: function () {
                return t.cookie ? t.cookie.split(";").map(function (e) {
                    return e.split("=")[0].trim()
                }) : []
            }
        }, JSON: e.JSON, getCssProperty: function (e) {
            for (var r = e.substr(0, 1), n = e.substr(1), a = r.toUpperCase() + n, o = r.toLowerCase() + n, i = [o, "Webkit" + a, "Moz" + a, "O" + a, "-ms-" + a, "ms" + a], s = t.documentElement.style, l = 0, c = i.length; l < c; l++) {
                var u = i[l];
                if (u in s) return u
            }
            return null
        }, makeArray: function (e) {
            return Array.prototype.slice.call(e)
        }, setVarByString: function (e, t, n) {
            var a = t.split(".");
            return function o(e, t) {
                var a = t.shift();
                t.length ? (e[a] === r && (e[a] = {}), o(e[a], t)) : e[a] = n
            }(e, a), e
        }, getVarByString: function (e, t) {
            for (var n = t.split("."), a = e, o = 0, i = n.length; o < i && a !== r; o++) a = a[n[o]];
            return a
        }, trace: {
            enable: ~location.href.indexOf("debug"), log: function () {
                if (this.enable && !(n.ie && n.ie < 8)) {
                    var e, t = a.makeArray(arguments);
                    t[0] = "[" + (new Date).toString().toLocaleString().replace(/^.* (\d+:\d+:\d+) .*$/, "$1") + "] " + t[0], "undefined" != typeof console && (n.ie ? (e = [], $(t).each(function (t, r) {
                        if ("string" == typeof r) e.push(r.replace(/%c/g, "").replace(/color:\s*[^;]+;/g, "")); else if ("object" == typeof r) try {
                            e.push(a.JSON.stringify(r))
                        } catch (n) {
                        } else e.push(r)
                    }), console.log(e.join(" "))) : console.log.apply(console, t))
                }
            }, ent: function () {
                var e = a.makeArray(arguments);
                e = ["%c[ent]", "color: #ffdd00;"].concat(e), this.log.apply(this, e)
            }, info: function () {
                var e = a.makeArray(arguments);
                e = ["%c[info]", "color: #005982;"].concat(e), this.log.apply(this, e)
            }, warn: function () {
                var e = a.makeArray(arguments);
                e = ["%c[warning]", "color: #8a8000;"].concat(e), this.log.apply(this, e)
            }, error: function () {
                var e = a.makeArray(arguments);
                e = ["%c[error]", "color: #ff0000;"].concat(e), this.log.apply(this, e)
            }, flash: function () {
                var e = a.makeArray(arguments);
                e = ["%c[flash]", "color: #7d0000;"].concat(e), this.log.apply(this, e)
            }, h5: function () {
                var e = a.makeArray(arguments);
                e = ["%c[h5]", "color: #ff8900;"].concat(e), this.log.apply(this, e)
            }, web: function () {
                var e = a.makeArray(arguments);
                e = ["%c[web]", "color: #556fb5;"].concat(e), this.log.apply(this, e)
            }, wf: function () {
                var e = a.makeArray(arguments);
                e = ["%c[web2flash]", "color: #7e0043;"].concat(e), this.log.apply(this, e)
            }, ajax: function () {
                var e = a.makeArray(arguments);
                e = ["%c[AJAX]", "color: #ff8900;"].concat(e), this.log.apply(this, e)
            }
        }, debounce: function (e, t, r) {
            var n;
            return function () {
                var a = this, o = arguments, i = function () {
                    n = null, r || e.apply(a, o)
                }, s = r && !n;
                clearTimeout(n), n = setTimeout(i, t), s && e.apply(a, o)
            }
        }, throttle: function (e, t, r) {
            var n, a, o, i = null, s = 0;
            r || (r = {});
            var l = function () {
                s = r.leading === !1 ? 0 : Date.now(), i = null, o = e.apply(n, a), i || (n = a = null)
            };
            return function () {
                var c = Date.now();
                s || r.leading !== !1 || (s = c);
                var u = t - (c - s);
                return n = this, a = arguments, u <= 0 || u > t ? (i && (clearTimeout(i), i = null), s = c, o = e.apply(n, a), i || (n = a = null)) : i || r.trailing === !1 || (i = setTimeout(l, u)), o
            }
        }, flattenProperty: function (e, t) {
            var r = null;
            for (var n in e[t]) {
                if (e[n]) throw new Error("[" + n + "] already exists in component!");
                r = e[t][n].bind(e), e[t][n] = r, e[n] = r
            }
        }, textCutOff: function (e, t) {
            var r = "", n = function (e) {
                for (var t = 0, r = /[\u4e00-\u9fa5]/, n = /[\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]/, a = e.length - 1; a >= 0; a--) t += r.test(e[a]) || n.test(e[a]) ? 1 : .5;
                return t
            }, a = n(e);
            return r = a <= t ? e : e.substr(0, t - 1) + "..."
        }, countDown: function (e) {
            var t, r, n, a, o = {time: 1e3, totalTime: 0, cb: null};
            n = $.extend({}, o, e), n.totalTime % n.time && (n.totalTime = Math.floor(n.totalTime / n.time) * n.time + n.time), a = {
                currentT: n.time || 0,
                totalTime: n.totalTime - n.time || 0
            };
            var i = function () {
                t = setTimeout(function () {
                    a.totalTime >= 0 ? (n.cb(a), a.totalTime -= n.time, a.currentT += n.time, i()) : clearTimeout(t)
                }, n.time)
            };
            return r = {
                start: function () {
                    t && clearTimeout(t), i()
                }, pause: function () {
                    t && clearTimeout(t)
                }, stop: function () {
                    t && clearTimeout(t), a.currentT = 0
                }, destory: function () {
                    t && clearTimeout(t), t = null, a.currentT = 0
                }
            }
        }
    };
    "undefined" != typeof define && define.amd ? define("util", [], function () {
        return a
    }) : e.util = a
}(window, document), !function () {
    function e(e) {
        return e.replace(w, "").replace(b, ",").replace(T, "").replace($, "").replace(_, "").split(C)
    }

    function t(e) {
        return "'" + e.replace(/('|\\)/g, "\\$1").replace(/\r/g, "\\r").replace(/\n/g, "\\n") + "'"
    }

    function r(r, n) {
        function a(e) {
            return f += e.split(/\n/).length - 1, u && (e = e.replace(/\s+/g, " ").replace(/<!--[\w\W]*?-->/g, "")), e && (e = y[1] + t(e) + y[2] + "\n"), e
        }

        function o(t) {
            var r = f;
            if (c ? t = c(t, n) : i && (t = t.replace(/\n/g, function () {
                return f++, "$line=" + f + ";"
            })), 0 === t.indexOf("=")) {
                var a = h && !/^=[=#]/.test(t);
                if (t = t.replace(/^=[=#]?|[\s;]*$/g, ""), a) {
                    var o = t.replace(/\s*\([^\)]+\)/, "");
                    p[o] || /^(include|print)$/.test(o) || (t = "$escape(" + t + ")")
                } else t = "$string(" + t + ")";
                t = y[1] + t + y[2]
            }
            return i && (t = "$line=" + r + ";" + t), v(e(t), function (e) {
                if (e && !m[e]) {
                    var t;
                    t = "print" === e ? b : "include" === e ? T : p[e] ? "$utils." + e : d[e] ? "$helpers." + e : "$data." + e, $ += e + "=" + t + ",", m[e] = !0
                }
            }), t + "\n"
        }

        var i = n.debug, s = n.openTag, l = n.closeTag, c = n.parser, u = n.compress, h = n.escape, f = 1,
            m = {$data: 1, $filename: 1, $utils: 1, $helpers: 1, $out: 1, $line: 1}, g = "".trim,
            y = g ? ["$out='';", "$out+=", ";", "$out"] : ["$out=[];", "$out.push(", ");", "$out.join('')"],
            w = g ? "$out+=text;return $out;" : "$out.push(text);",
            b = "function(){var text=''.concat.apply('',arguments);" + w + "}",
            T = "function(filename,data){data=data||$data;var text=$utils.$include(filename,data,$filename);" + w + "}",
            $ = "'use strict';var $utils=this,$helpers=$utils.$helpers," + (i ? "$line=0," : ""), _ = y[0],
            C = "return new String(" + y[3] + ");";
        v(r.split(s), function (e) {
            e = e.split(l);
            var t = e[0], r = e[1];
            1 === e.length ? _ += a(t) : (_ += o(t), r && (_ += a(r)))
        });
        var k = $ + _ + C;
        i && (k = "try{" + k + "}catch(e){throw {filename:$filename,name:'Render Error',message:e.message,line:$line,source:" + t(r) + ".split(/\\n/)[$line-1].replace(/^\\s+/,'')};}");
        try {
            var A = new Function("$data", "$filename", k);
            return A.prototype = p, A
        } catch (E) {
            throw E.temp = "function anonymous($data,$filename) {" + k + "}", E
        }
    }

    var n = function (e, t) {
        return "string" == typeof t ? g(t, {filename: e}) : i(e, t)
    };
    n.version = "3.0.0", n.config = function (e, t) {
        a[e] = t
    };
    var a = n.defaults = {openTag: "<%", closeTag: "%>", escape: !0, cache: !0, compress: !1, parser: null},
        o = n.cache = {};
    n.render = function (e, t) {
        return g(e, t)
    };
    var i = n.renderFile = function (e, t) {
        var r = n.get(e) || m({filename: e, name: "Render Error", message: "Template not found"});
        return t ? r(t) : r
    };
    n.get = function (e) {
        var t;
        if (o[e]) t = o[e]; else if ("object" == typeof document) {
            var r = document.getElementById(e);
            if (r) {
                var n = (r.value || r.innerHTML).replace(/^\s*|\s*$/g, "");
                t = g(n, {filename: e})
            }
        }
        return t
    };
    var s = function (e, t) {
        return "string" != typeof e && (t = typeof e, "number" === t ? e += "" : e = "function" === t ? s(e.call(e)) : ""), e
    }, l = {"<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "&": "&#38;"}, c = function (e) {
        return l[e]
    }, u = function (e) {
        return s(e).replace(/&(?![\w#]+;)|[<>"']/g, c)
    }, h = Array.isArray || function (e) {
        return "[object Array]" === {}.toString.call(e)
    }, f = function (e, t) {
        var r, n;
        if (h(e)) for (r = 0, n = e.length; n > r; r++) t.call(e, e[r], r, e); else for (r in e) t.call(e, e[r], r)
    }, p = n.utils = {$helpers: {}, $include: i, $string: s, $escape: u, $each: f};
    n.helper = function (e, t) {
        d[e] = t
    };
    var d = n.helpers = p.$helpers;
    n.onerror = function (e) {
        var t = "Template Error\n\n";
        for (var r in e) t += "<" + r + ">\n" + e[r] + "\n\n";
        "object" == typeof console && console.error(t)
    };
    var m = function (e) {
            return n.onerror(e), function () {
                return "{Template Error}"
            }
        }, g = n.compile = function (e, t) {
            function n(r) {
                try {
                    return new l(r, s) + ""
                } catch (n) {
                    return t.debug ? m(n)() : (t.debug = !0, g(e, t)(r))
                }
            }

            t = t || {};
            for (var i in a) void 0 === t[i] && (t[i] = a[i]);
            var s = t.filename;
            try {
                var l = r(e, t)
            } catch (c) {
                return c.filename = s || "anonymous", c.name = "Syntax Error", m(c)
            }
            return n.prototype = l.prototype, n.toString = function () {
                return l.toString()
            }, s && t.cache && (o[s] = n), n
        }, v = p.$each,
        y = "break,case,catch,continue,debugger,default,delete,do,else,false,finally,for,function,if,in,instanceof,new,null,return,switch,this,throw,true,try,typeof,var,void,while,with,abstract,boolean,byte,char,class,const,double,enum,export,extends,final,float,goto,implements,import,int,interface,long,native,package,private,protected,public,short,static,super,synchronized,throws,transient,volatile,arguments,let,yield,undefined",
        w = /\/\*[\w\W]*?\*\/|\/\/[^\n]*\n|\/\/[^\n]*$|"(?:[^"\\]|\\[\w\W])*"|'(?:[^'\\]|\\[\w\W])*'|\s*\.\s*[$\w\.]+/g,
        b = /[^\w$]+/g, T = new RegExp(["\\b" + y.replace(/,/g, "\\b|\\b") + "\\b"].join("|"), "g"),
        $ = /^\d[^,]*|,\d[^,]*/g, _ = /^,+|,+$/g, C = /^$|,+/;
    a.openTag = "{{", a.closeTag = "}}";
    var k = function (e, t) {
        var r = t.split(":"), n = r.shift(), a = r.join(":") || "";
        return a && (a = ", " + a), "$helpers." + n + "(" + e + a + ")"
    };
    a.parser = function (e) {
        e = e.replace(/^\s/, "");
        var t = e.split(" "), r = t.shift(), a = t.join(" ");
        switch (r) {
            case"if":
                e = "if(" + a + "){";
                break;
            case"else":
                t = "if" === t.shift() ? " if(" + t.join(" ") + ")" : "", e = "}else" + t + "{";
                break;
            case"/if":
                e = "}";
                break;
            case"each":
                var o = t[0] || "$data", i = t[1] || "as", s = t[2] || "$value", l = t[3] || "$index", c = s + "," + l;
                "as" !== i && (o = "[]"), e = "$each(" + o + ",function(" + c + "){";
                break;
            case"/each":
                e = "});";
                break;
            case"echo":
                e = "print(" + a + ");";
                break;
            case"print":
            case"include":
                e = r + "(" + t.join(",") + ");";
                break;
            default:
                if (/^\s*\|\s*[\w\$]/.test(a)) {
                    var u = !0;
                    0 === e.indexOf("#") && (e = e.substr(1), u = !1);
                    for (var h = 0, f = e.split("|"), p = f.length, d = f[h++]; p > h; h++) d = k(d, f[h]);
                    e = (u ? "=" : "=#") + d
                } else e = n.helpers[r] ? "=#" + r + "(" + t.join(",") + ");" : "=" + e
        }
        return e
    }, "function" == typeof define ? define("artTemplate", [], function () {
        return n
    }) : "undefined" != typeof exports ? module.exports = n : this.template = n
}(), define("QRCode", [], function () {
    function e(e) {
        this.mode = u.MODE_8BIT_BYTE, this.data = e, this.parsedData = [];
        for (var t = 0, r = this.data.length; t < r; t++) {
            var n = [], a = this.data.charCodeAt(t);
            a > 65536 ? (n[0] = 240 | (1835008 & a) >>> 18, n[1] = 128 | (258048 & a) >>> 12, n[2] = 128 | (4032 & a) >>> 6, n[3] = 128 | 63 & a) : a > 2048 ? (n[0] = 224 | (61440 & a) >>> 12, n[1] = 128 | (4032 & a) >>> 6, n[2] = 128 | 63 & a) : a > 128 ? (n[0] = 192 | (1984 & a) >>> 6, n[1] = 128 | 63 & a) : n[0] = a, this.parsedData.push(n)
        }
        this.parsedData = Array.prototype.concat.apply([], this.parsedData), this.parsedData.length != this.data.length && (this.parsedData.unshift(191), this.parsedData.unshift(187), this.parsedData.unshift(239))
    }

    function t(e, t) {
        this.typeNumber = e, this.errorCorrectLevel = t, this.modules = null, this.moduleCount = 0, this.dataCache = null, this.dataList = []
    }

    function r(e, t) {
        if (void 0 == e.length) throw new Error(e.length + "/" + t);
        for (var r = 0; r < e.length && 0 == e[r];) r++;
        this.num = new Array(e.length - r + t);
        for (var n = 0; n < e.length - r; n++) this.num[n] = e[n + r]
    }

    function n(e, t) {
        this.totalCount = e, this.dataCount = t
    }

    function a() {
        this.buffer = [], this.length = 0
    }

    function o() {
        return "undefined" != typeof CanvasRenderingContext2D
    }

    function i() {
        var e = !1, t = navigator.userAgent;
        if (/android/i.test(t)) {
            e = !0;
            var r = t.toString().match(/android ([0-9]\.[0-9])/i);
            r && r[1] && (e = parseFloat(r[1]))
        }
        return e
    }

    function s(e, t) {
        for (var r = 1, n = l(e), a = 0, o = g.length; a <= o; a++) {
            var i = 0;
            switch (t) {
                case h.L:
                    i = g[a][0];
                    break;
                case h.M:
                    i = g[a][1];
                    break;
                case h.Q:
                    i = g[a][2];
                    break;
                case h.H:
                    i = g[a][3]
            }
            if (n <= i) break;
            r++
        }
        if (r > g.length) throw new Error("Too long data");
        return r
    }

    function l(e) {
        var t = encodeURI(e).toString().replace(/\%[0-9a-fA-F]{2}/g, "a");
        return t.length + (t.length != e ? 3 : 0)
    }

    var c;
    e.prototype = {
        getLength: function (e) {
            return this.parsedData.length
        }, write: function (e) {
            for (var t = 0, r = this.parsedData.length; t < r; t++) e.put(this.parsedData[t], 8)
        }
    }, t.prototype = {
        addData: function (t) {
            var r = new e(t);
            this.dataList.push(r), this.dataCache = null
        }, isDark: function (e, t) {
            if (e < 0 || this.moduleCount <= e || t < 0 || this.moduleCount <= t) throw new Error(e + "," + t);
            return this.modules[e][t]
        }, getModuleCount: function () {
            return this.moduleCount
        }, make: function () {
            this.makeImpl(!1, this.getBestMaskPattern())
        }, makeImpl: function (e, r) {
            this.moduleCount = 4 * this.typeNumber + 17, this.modules = new Array(this.moduleCount);
            for (var n = 0; n < this.moduleCount; n++) {
                this.modules[n] = new Array(this.moduleCount);
                for (var a = 0; a < this.moduleCount; a++) this.modules[n][a] = null
            }
            this.setupPositionProbePattern(0, 0), this.setupPositionProbePattern(this.moduleCount - 7, 0), this.setupPositionProbePattern(0, this.moduleCount - 7), this.setupPositionAdjustPattern(), this.setupTimingPattern(), this.setupTypeInfo(e, r), this.typeNumber >= 7 && this.setupTypeNumber(e), null == this.dataCache && (this.dataCache = t.createData(this.typeNumber, this.errorCorrectLevel, this.dataList)), this.mapData(this.dataCache, r)
        }, setupPositionProbePattern: function (e, t) {
            for (var r = -1; r <= 7; r++) if (!(e + r <= -1 || this.moduleCount <= e + r)) for (var n = -1; n <= 7; n++) t + n <= -1 || this.moduleCount <= t + n || (0 <= r && r <= 6 && (0 == n || 6 == n) || 0 <= n && n <= 6 && (0 == r || 6 == r) || 2 <= r && r <= 4 && 2 <= n && n <= 4 ? this.modules[e + r][t + n] = !0 : this.modules[e + r][t + n] = !1)
        }, getBestMaskPattern: function () {
            for (var e = 0, t = 0, r = 0; r < 8; r++) {
                this.makeImpl(!0, r);
                var n = p.getLostPoint(this);
                (0 == r || e > n) && (e = n, t = r)
            }
            return t
        }, createMovieClip: function (e, t, r) {
            var n = e.createEmptyMovieClip(t, r), a = 1;
            this.make();
            for (var o = 0; o < this.modules.length; o++) for (var i = o * a, s = 0; s < this.modules[o].length; s++) {
                var l = s * a, c = this.modules[o][s];
                c && (n.beginFill(0, 100), n.moveTo(l, i), n.lineTo(l + a, i), n.lineTo(l + a, i + a), n.lineTo(l, i + a), n.endFill())
            }
            return n
        }, setupTimingPattern: function () {
            for (var e = 8; e < this.moduleCount - 8; e++) null == this.modules[e][6] && (this.modules[e][6] = e % 2 == 0);
            for (var t = 8; t < this.moduleCount - 8; t++) null == this.modules[6][t] && (this.modules[6][t] = t % 2 == 0)
        }, setupPositionAdjustPattern: function () {
            for (var e = p.getPatternPosition(this.typeNumber), t = 0; t < e.length; t++) for (var r = 0; r < e.length; r++) {
                var n = e[t], a = e[r];
                if (null == this.modules[n][a]) for (var o = -2; o <= 2; o++) for (var i = -2; i <= 2; i++) o == -2 || 2 == o || i == -2 || 2 == i || 0 == o && 0 == i ? this.modules[n + o][a + i] = !0 : this.modules[n + o][a + i] = !1
            }
        }, setupTypeNumber: function (e) {
            for (var t = p.getBCHTypeNumber(this.typeNumber), r = 0; r < 18; r++) {
                var n = !e && 1 == (t >> r & 1);
                this.modules[Math.floor(r / 3)][r % 3 + this.moduleCount - 8 - 3] = n
            }
            for (var r = 0; r < 18; r++) {
                var n = !e && 1 == (t >> r & 1);
                this.modules[r % 3 + this.moduleCount - 8 - 3][Math.floor(r / 3)] = n
            }
        }, setupTypeInfo: function (e, t) {
            for (var r = this.errorCorrectLevel << 3 | t, n = p.getBCHTypeInfo(r), a = 0; a < 15; a++) {
                var o = !e && 1 == (n >> a & 1);
                a < 6 ? this.modules[a][8] = o : a < 8 ? this.modules[a + 1][8] = o : this.modules[this.moduleCount - 15 + a][8] = o
            }
            for (var a = 0; a < 15; a++) {
                var o = !e && 1 == (n >> a & 1);
                a < 8 ? this.modules[8][this.moduleCount - a - 1] = o : a < 9 ? this.modules[8][15 - a - 1 + 1] = o : this.modules[8][15 - a - 1] = o
            }
            this.modules[this.moduleCount - 8][8] = !e
        }, mapData: function (e, t) {
            for (var r = -1, n = this.moduleCount - 1, a = 7, o = 0, i = this.moduleCount - 1; i > 0; i -= 2) for (6 == i && i--; ;) {
                for (var s = 0; s < 2; s++) if (null == this.modules[n][i - s]) {
                    var l = !1;
                    o < e.length && (l = 1 == (e[o] >>> a & 1));
                    var c = p.getMask(t, n, i - s);
                    c && (l = !l), this.modules[n][i - s] = l, a--, a == -1 && (o++, a = 7)
                }
                if (n += r, n < 0 || this.moduleCount <= n) {
                    n -= r, r = -r;
                    break
                }
            }
        }
    }, t.PAD0 = 236, t.PAD1 = 17, t.createData = function (e, r, o) {
        for (var i = n.getRSBlocks(e, r), s = new a, l = 0; l < o.length; l++) {
            var c = o[l];
            s.put(c.mode, 4), s.put(c.getLength(), p.getLengthInBits(c.mode, e)), c.write(s)
        }
        for (var u = 0, l = 0; l < i.length; l++) u += i[l].dataCount;
        if (s.getLengthInBits() > 8 * u) throw new Error("code length overflow. (" + s.getLengthInBits() + ">" + 8 * u + ")");
        for (s.getLengthInBits() + 4 <= 8 * u && s.put(0, 4); s.getLengthInBits() % 8 != 0;) s.putBit(!1);
        for (; ;) {
            if (s.getLengthInBits() >= 8 * u) break;
            if (s.put(t.PAD0, 8), s.getLengthInBits() >= 8 * u) break;
            s.put(t.PAD1, 8)
        }
        return t.createBytes(s, i)
    }, t.createBytes = function (e, t) {
        for (var n = 0, a = 0, o = 0, i = new Array(t.length), s = new Array(t.length), l = 0; l < t.length; l++) {
            var c = t[l].dataCount, u = t[l].totalCount - c;
            a = Math.max(a, c), o = Math.max(o, u), i[l] = new Array(c);
            for (var h = 0; h < i[l].length; h++) i[l][h] = 255 & e.buffer[h + n];
            n += c;
            var f = p.getErrorCorrectPolynomial(u), d = new r(i[l], f.getLength() - 1), m = d.mod(f);
            s[l] = new Array(f.getLength() - 1);
            for (var h = 0; h < s[l].length; h++) {
                var g = h + m.getLength() - s[l].length;
                s[l][h] = g >= 0 ? m.get(g) : 0
            }
        }
        for (var v = 0, h = 0; h < t.length; h++) v += t[h].totalCount;
        for (var y = new Array(v), w = 0, h = 0; h < a; h++) for (var l = 0; l < t.length; l++) h < i[l].length && (y[w++] = i[l][h]);
        for (var h = 0; h < o; h++) for (var l = 0; l < t.length; l++) h < s[l].length && (y[w++] = s[l][h]);
        return y
    };
    for (var u = {MODE_NUMBER: 1, MODE_ALPHA_NUM: 2, MODE_8BIT_BYTE: 4, MODE_KANJI: 8}, h = {
        L: 1,
        M: 0,
        Q: 3,
        H: 2
    }, f = {
        PATTERN000: 0,
        PATTERN001: 1,
        PATTERN010: 2,
        PATTERN011: 3,
        PATTERN100: 4,
        PATTERN101: 5,
        PATTERN110: 6,
        PATTERN111: 7
    }, p = {
        PATTERN_POSITION_TABLE: [[], [6, 18], [6, 22], [6, 26], [6, 30], [6, 34], [6, 22, 38], [6, 24, 42], [6, 26, 46], [6, 28, 50], [6, 30, 54], [6, 32, 58], [6, 34, 62], [6, 26, 46, 66], [6, 26, 48, 70], [6, 26, 50, 74], [6, 30, 54, 78], [6, 30, 56, 82], [6, 30, 58, 86], [6, 34, 62, 90], [6, 28, 50, 72, 94], [6, 26, 50, 74, 98], [6, 30, 54, 78, 102], [6, 28, 54, 80, 106], [6, 32, 58, 84, 110], [6, 30, 58, 86, 114], [6, 34, 62, 90, 118], [6, 26, 50, 74, 98, 122], [6, 30, 54, 78, 102, 126], [6, 26, 52, 78, 104, 130], [6, 30, 56, 82, 108, 134], [6, 34, 60, 86, 112, 138], [6, 30, 58, 86, 114, 142], [6, 34, 62, 90, 118, 146], [6, 30, 54, 78, 102, 126, 150], [6, 24, 50, 76, 102, 128, 154], [6, 28, 54, 80, 106, 132, 158], [6, 32, 58, 84, 110, 136, 162], [6, 26, 54, 82, 110, 138, 166], [6, 30, 58, 86, 114, 142, 170]],
        G15: 1335,
        G18: 7973,
        G15_MASK: 21522,
        getBCHTypeInfo: function (e) {
            for (var t = e << 10; p.getBCHDigit(t) - p.getBCHDigit(p.G15) >= 0;) t ^= p.G15 << p.getBCHDigit(t) - p.getBCHDigit(p.G15);
            return (e << 10 | t) ^ p.G15_MASK
        },
        getBCHTypeNumber: function (e) {
            for (var t = e << 12; p.getBCHDigit(t) - p.getBCHDigit(p.G18) >= 0;) t ^= p.G18 << p.getBCHDigit(t) - p.getBCHDigit(p.G18);
            return e << 12 | t
        },
        getBCHDigit: function (e) {
            for (var t = 0; 0 != e;) t++, e >>>= 1;
            return t
        },
        getPatternPosition: function (e) {
            return p.PATTERN_POSITION_TABLE[e - 1]
        },
        getMask: function (e, t, r) {
            switch (e) {
                case f.PATTERN000:
                    return (t + r) % 2 == 0;
                case f.PATTERN001:
                    return t % 2 == 0;
                case f.PATTERN010:
                    return r % 3 == 0;
                case f.PATTERN011:
                    return (t + r) % 3 == 0;
                case f.PATTERN100:
                    return (Math.floor(t / 2) + Math.floor(r / 3)) % 2 == 0;
                case f.PATTERN101:
                    return t * r % 2 + t * r % 3 == 0;
                case f.PATTERN110:
                    return (t * r % 2 + t * r % 3) % 2 == 0;
                case f.PATTERN111:
                    return (t * r % 3 + (t + r) % 2) % 2 == 0;
                default:
                    throw new Error("bad maskPattern:" + e)
            }
        },
        getErrorCorrectPolynomial: function (e) {
            for (var t = new r([1], 0), n = 0; n < e; n++) t = t.multiply(new r([1, d.gexp(n)], 0));
            return t
        },
        getLengthInBits: function (e, t) {
            if (1 <= t && t < 10) switch (e) {
                case u.MODE_NUMBER:
                    return 10;
                case u.MODE_ALPHA_NUM:
                    return 9;
                case u.MODE_8BIT_BYTE:
                    return 8;
                case u.MODE_KANJI:
                    return 8;
                default:
                    throw new Error("mode:" + e)
            } else if (t < 27) switch (e) {
                case u.MODE_NUMBER:
                    return 12;
                case u.MODE_ALPHA_NUM:
                    return 11;
                case u.MODE_8BIT_BYTE:
                    return 16;
                case u.MODE_KANJI:
                    return 10;
                default:
                    throw new Error("mode:" + e)
            } else {
                if (!(t < 41)) throw new Error("type:" + t);
                switch (e) {
                    case u.MODE_NUMBER:
                        return 14;
                    case u.MODE_ALPHA_NUM:
                        return 13;
                    case u.MODE_8BIT_BYTE:
                        return 16;
                    case u.MODE_KANJI:
                        return 12;
                    default:
                        throw new Error("mode:" + e)
                }
            }
        },
        getLostPoint: function (e) {
            for (var t = e.getModuleCount(), r = 0, n = 0; n < t; n++) for (var a = 0; a < t; a++) {
                for (var o = 0, i = e.isDark(n, a), s = -1; s <= 1; s++) if (!(n + s < 0 || t <= n + s)) for (var l = -1; l <= 1; l++) a + l < 0 || t <= a + l || 0 == s && 0 == l || i == e.isDark(n + s, a + l) && o++;
                o > 5 && (r += 3 + o - 5)
            }
            for (var n = 0; n < t - 1; n++) for (var a = 0; a < t - 1; a++) {
                var c = 0;
                e.isDark(n, a) && c++, e.isDark(n + 1, a) && c++, e.isDark(n, a + 1) && c++, e.isDark(n + 1, a + 1) && c++, 0 != c && 4 != c || (r += 3)
            }
            for (var n = 0; n < t; n++) for (var a = 0; a < t - 6; a++) e.isDark(n, a) && !e.isDark(n, a + 1) && e.isDark(n, a + 2) && e.isDark(n, a + 3) && e.isDark(n, a + 4) && !e.isDark(n, a + 5) && e.isDark(n, a + 6) && (r += 40);
            for (var a = 0; a < t; a++) for (var n = 0; n < t - 6; n++) e.isDark(n, a) && !e.isDark(n + 1, a) && e.isDark(n + 2, a) && e.isDark(n + 3, a) && e.isDark(n + 4, a) && !e.isDark(n + 5, a) && e.isDark(n + 6, a) && (r += 40);
            for (var u = 0, a = 0; a < t; a++) for (var n = 0; n < t; n++) e.isDark(n, a) && u++;
            var h = Math.abs(100 * u / t / t - 50) / 5;
            return r += 10 * h
        }
    }, d = {
        glog: function (e) {
            if (e < 1) throw new Error("glog(" + e + ")");
            return d.LOG_TABLE[e]
        }, gexp: function (e) {
            for (; e < 0;) e += 255;
            for (; e >= 256;) e -= 255;
            return d.EXP_TABLE[e]
        }, EXP_TABLE: new Array(256), LOG_TABLE: new Array(256)
    }, m = 0; m < 8; m++) d.EXP_TABLE[m] = 1 << m;
    for (var m = 8; m < 256; m++) d.EXP_TABLE[m] = d.EXP_TABLE[m - 4] ^ d.EXP_TABLE[m - 5] ^ d.EXP_TABLE[m - 6] ^ d.EXP_TABLE[m - 8];
    for (var m = 0; m < 255; m++) d.LOG_TABLE[d.EXP_TABLE[m]] = m;
    r.prototype = {
        get: function (e) {
            return this.num[e]
        }, getLength: function () {
            return this.num.length
        }, multiply: function (e) {
            for (var t = new Array(this.getLength() + e.getLength() - 1), n = 0; n < this.getLength(); n++) for (var a = 0; a < e.getLength(); a++) t[n + a] ^= d.gexp(d.glog(this.get(n)) + d.glog(e.get(a)));
            return new r(t, 0)
        }, mod: function (e) {
            if (this.getLength() - e.getLength() < 0) return this;
            for (var t = d.glog(this.get(0)) - d.glog(e.get(0)), n = new Array(this.getLength()), a = 0; a < this.getLength(); a++) n[a] = this.get(a);
            for (var a = 0; a < e.getLength(); a++) n[a] ^= d.gexp(d.glog(e.get(a)) + t);
            return new r(n, 0).mod(e)
        }
    }, n.RS_BLOCK_TABLE = [[1, 26, 19], [1, 26, 16], [1, 26, 13], [1, 26, 9], [1, 44, 34], [1, 44, 28], [1, 44, 22], [1, 44, 16], [1, 70, 55], [1, 70, 44], [2, 35, 17], [2, 35, 13], [1, 100, 80], [2, 50, 32], [2, 50, 24], [4, 25, 9], [1, 134, 108], [2, 67, 43], [2, 33, 15, 2, 34, 16], [2, 33, 11, 2, 34, 12], [2, 86, 68], [4, 43, 27], [4, 43, 19], [4, 43, 15], [2, 98, 78], [4, 49, 31], [2, 32, 14, 4, 33, 15], [4, 39, 13, 1, 40, 14], [2, 121, 97], [2, 60, 38, 2, 61, 39], [4, 40, 18, 2, 41, 19], [4, 40, 14, 2, 41, 15], [2, 146, 116], [3, 58, 36, 2, 59, 37], [4, 36, 16, 4, 37, 17], [4, 36, 12, 4, 37, 13], [2, 86, 68, 2, 87, 69], [4, 69, 43, 1, 70, 44], [6, 43, 19, 2, 44, 20], [6, 43, 15, 2, 44, 16], [4, 101, 81], [1, 80, 50, 4, 81, 51], [4, 50, 22, 4, 51, 23], [3, 36, 12, 8, 37, 13], [2, 116, 92, 2, 117, 93], [6, 58, 36, 2, 59, 37], [4, 46, 20, 6, 47, 21], [7, 42, 14, 4, 43, 15], [4, 133, 107], [8, 59, 37, 1, 60, 38], [8, 44, 20, 4, 45, 21], [12, 33, 11, 4, 34, 12], [3, 145, 115, 1, 146, 116], [4, 64, 40, 5, 65, 41], [11, 36, 16, 5, 37, 17], [11, 36, 12, 5, 37, 13], [5, 109, 87, 1, 110, 88], [5, 65, 41, 5, 66, 42], [5, 54, 24, 7, 55, 25], [11, 36, 12], [5, 122, 98, 1, 123, 99], [7, 73, 45, 3, 74, 46], [15, 43, 19, 2, 44, 20], [3, 45, 15, 13, 46, 16], [1, 135, 107, 5, 136, 108], [10, 74, 46, 1, 75, 47], [1, 50, 22, 15, 51, 23], [2, 42, 14, 17, 43, 15], [5, 150, 120, 1, 151, 121], [9, 69, 43, 4, 70, 44], [17, 50, 22, 1, 51, 23], [2, 42, 14, 19, 43, 15], [3, 141, 113, 4, 142, 114], [3, 70, 44, 11, 71, 45], [17, 47, 21, 4, 48, 22], [9, 39, 13, 16, 40, 14], [3, 135, 107, 5, 136, 108], [3, 67, 41, 13, 68, 42], [15, 54, 24, 5, 55, 25], [15, 43, 15, 10, 44, 16], [4, 144, 116, 4, 145, 117], [17, 68, 42], [17, 50, 22, 6, 51, 23], [19, 46, 16, 6, 47, 17], [2, 139, 111, 7, 140, 112], [17, 74, 46], [7, 54, 24, 16, 55, 25], [34, 37, 13], [4, 151, 121, 5, 152, 122], [4, 75, 47, 14, 76, 48], [11, 54, 24, 14, 55, 25], [16, 45, 15, 14, 46, 16], [6, 147, 117, 4, 148, 118], [6, 73, 45, 14, 74, 46], [11, 54, 24, 16, 55, 25], [30, 46, 16, 2, 47, 17], [8, 132, 106, 4, 133, 107], [8, 75, 47, 13, 76, 48], [7, 54, 24, 22, 55, 25], [22, 45, 15, 13, 46, 16], [10, 142, 114, 2, 143, 115], [19, 74, 46, 4, 75, 47], [28, 50, 22, 6, 51, 23], [33, 46, 16, 4, 47, 17], [8, 152, 122, 4, 153, 123], [22, 73, 45, 3, 74, 46], [8, 53, 23, 26, 54, 24], [12, 45, 15, 28, 46, 16], [3, 147, 117, 10, 148, 118], [3, 73, 45, 23, 74, 46], [4, 54, 24, 31, 55, 25], [11, 45, 15, 31, 46, 16], [7, 146, 116, 7, 147, 117], [21, 73, 45, 7, 74, 46], [1, 53, 23, 37, 54, 24], [19, 45, 15, 26, 46, 16], [5, 145, 115, 10, 146, 116], [19, 75, 47, 10, 76, 48], [15, 54, 24, 25, 55, 25], [23, 45, 15, 25, 46, 16], [13, 145, 115, 3, 146, 116], [2, 74, 46, 29, 75, 47], [42, 54, 24, 1, 55, 25], [23, 45, 15, 28, 46, 16], [17, 145, 115], [10, 74, 46, 23, 75, 47], [10, 54, 24, 35, 55, 25], [19, 45, 15, 35, 46, 16], [17, 145, 115, 1, 146, 116], [14, 74, 46, 21, 75, 47], [29, 54, 24, 19, 55, 25], [11, 45, 15, 46, 46, 16], [13, 145, 115, 6, 146, 116], [14, 74, 46, 23, 75, 47], [44, 54, 24, 7, 55, 25], [59, 46, 16, 1, 47, 17], [12, 151, 121, 7, 152, 122], [12, 75, 47, 26, 76, 48], [39, 54, 24, 14, 55, 25], [22, 45, 15, 41, 46, 16], [6, 151, 121, 14, 152, 122], [6, 75, 47, 34, 76, 48], [46, 54, 24, 10, 55, 25], [2, 45, 15, 64, 46, 16], [17, 152, 122, 4, 153, 123], [29, 74, 46, 14, 75, 47], [49, 54, 24, 10, 55, 25], [24, 45, 15, 46, 46, 16], [4, 152, 122, 18, 153, 123], [13, 74, 46, 32, 75, 47], [48, 54, 24, 14, 55, 25], [42, 45, 15, 32, 46, 16], [20, 147, 117, 4, 148, 118], [40, 75, 47, 7, 76, 48], [43, 54, 24, 22, 55, 25], [10, 45, 15, 67, 46, 16], [19, 148, 118, 6, 149, 119], [18, 75, 47, 31, 76, 48], [34, 54, 24, 34, 55, 25], [20, 45, 15, 61, 46, 16]],
        n.getRSBlocks = function (e, t) {
            var r = n.getRsBlockTable(e, t);
            if (void 0 == r) throw new Error("bad rs block @ typeNumber:" + e + "/errorCorrectLevel:" + t);
            for (var a = r.length / 3, o = [], i = 0; i < a; i++) for (var s = r[3 * i + 0], l = r[3 * i + 1], c = r[3 * i + 2], u = 0; u < s; u++) o.push(new n(l, c));
            return o
        }, n.getRsBlockTable = function (e, t) {
        switch (t) {
            case h.L:
                return n.RS_BLOCK_TABLE[4 * (e - 1) + 0];
            case h.M:
                return n.RS_BLOCK_TABLE[4 * (e - 1) + 1];
            case h.Q:
                return n.RS_BLOCK_TABLE[4 * (e - 1) + 2];
            case h.H:
                return n.RS_BLOCK_TABLE[4 * (e - 1) + 3];
            default:
                return
        }
    }, a.prototype = {
        get: function (e) {
            var t = Math.floor(e / 8);
            return 1 == (this.buffer[t] >>> 7 - e % 8 & 1)
        }, put: function (e, t) {
            for (var r = 0; r < t; r++) this.putBit(1 == (e >>> t - r - 1 & 1))
        }, getLengthInBits: function () {
            return this.length
        }, putBit: function (e) {
            var t = Math.floor(this.length / 8);
            this.buffer.length <= t && this.buffer.push(0), e && (this.buffer[t] |= 128 >>> this.length % 8), this.length++
        }
    };
    var g = [[17, 14, 11, 7], [32, 26, 20, 14], [53, 42, 32, 24], [78, 62, 46, 34], [106, 84, 60, 44], [134, 106, 74, 58], [154, 122, 86, 64], [192, 152, 108, 84], [230, 180, 130, 98], [271, 213, 151, 119], [321, 251, 177, 137], [367, 287, 203, 155], [425, 331, 241, 177], [458, 362, 258, 194], [520, 412, 292, 220], [586, 450, 322, 250], [644, 504, 364, 280], [718, 560, 394, 310], [792, 624, 442, 338], [858, 666, 482, 382], [929, 711, 509, 403], [1003, 779, 565, 439], [1091, 857, 611, 461], [1171, 911, 661, 511], [1273, 997, 715, 535], [1367, 1059, 751, 593], [1465, 1125, 805, 625], [1528, 1190, 868, 658], [1628, 1264, 908, 698], [1732, 1370, 982, 742], [1840, 1452, 1030, 790], [1952, 1538, 1112, 842], [2068, 1628, 1168, 898], [2188, 1722, 1228, 958], [2303, 1809, 1283, 983], [2431, 1911, 1351, 1051], [2563, 1989, 1423, 1093], [2699, 2099, 1499, 1139], [2809, 2213, 1579, 1219], [2953, 2331, 1663, 1273]],
        v = function () {
            var e = function (e, t) {
                this._el = e, this._htOption = t
            };
            return e.prototype.draw = function (e) {
                function t(e, t) {
                    var r = document.createElementNS("http://www.w3.org/2000/svg", e);
                    for (var n in t) t.hasOwnProperty(n) && r.setAttribute(n, t[n]);
                    return r
                }

                var r = this._htOption, n = this._el, a = e.getModuleCount();
                Math.floor(r.width / a), Math.floor(r.height / a);
                this.clear();
                var o = t("svg", {
                    viewBox: "0 0 " + String(a) + " " + String(a),
                    width: "100%",
                    height: "100%",
                    fill: r.colorLight
                });
                o.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink"), n.appendChild(o), o.appendChild(t("rect", {
                    fill: r.colorLight,
                    width: "100%",
                    height: "100%"
                })), o.appendChild(t("rect", {fill: r.colorDark, width: "1", height: "1", id: "template"}));
                for (var i = 0; i < a; i++) for (var s = 0; s < a; s++) if (e.isDark(i, s)) {
                    var l = t("use", {x: String(s), y: String(i)});
                    l.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#template"), o.appendChild(l)
                }
            }, e.prototype.clear = function () {
                for (; this._el.hasChildNodes();) this._el.removeChild(this._el.lastChild)
            }, e
        }(), y = "svg" === document.documentElement.tagName.toLowerCase(), w = y ? v : o() ? function () {
            function e() {
                this._elImage.src = this._elCanvas.toDataURL("image/png"), this._elImage.style.display = "block", this._elCanvas.style.display = "none"
            }

            function t(e, t) {
                var r = this;
                if (r._fFail = t, r._fSuccess = e, null === r._bSupportDataURI) {
                    var n = document.createElement("img"), a = function () {
                        r._bSupportDataURI = !1, r._fFail && r._fFail.call(r)
                    }, o = function () {
                        r._bSupportDataURI = !0, r._fSuccess && r._fSuccess.call(r)
                    };
                    return n.onabort = a, n.onerror = a, n.onload = o, void(n.src = "data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==")
                }
                r._bSupportDataURI === !0 && r._fSuccess ? r._fSuccess.call(r) : r._bSupportDataURI === !1 && r._fFail && r._fFail.call(r)
            }

            if (this._android && this._android <= 2.1) {
                var r = 1 / window.devicePixelRatio, n = CanvasRenderingContext2D.prototype.drawImage;
                CanvasRenderingContext2D.prototype.drawImage = function (e, t, a, o, i, s, l, c, u) {
                    if ("nodeName" in e && /img/i.test(e.nodeName)) for (var h = arguments.length - 1; h >= 1; h--) arguments[h] = arguments[h] * r; else "undefined" == typeof c && (arguments[1] *= r, arguments[2] *= r, arguments[3] *= r, arguments[4] *= r);
                    n.apply(this, arguments)
                }
            }
            var a = function (e, t) {
                this._bIsPainted = !1, this._android = i(), this._htOption = t, this._elCanvas = document.createElement("canvas"), this._elCanvas.width = t.width, this._elCanvas.height = t.height, e.appendChild(this._elCanvas), this._el = e, this._oContext = this._elCanvas.getContext("2d"), this._bIsPainted = !1, this._elImage = document.createElement("img"), this._elImage.alt = "Scan me!", this._elImage.style.display = "none", this._el.appendChild(this._elImage), this._bSupportDataURI = null
            };
            return a.prototype.draw = function (e) {
                var t = this._elImage, r = this._oContext, n = this._htOption, a = e.getModuleCount(), o = n.width / a,
                    i = n.height / a, s = Math.round(o), l = Math.round(i);
                t.style.display = "none", this.clear();
                for (var c = 0; c < a; c++) for (var u = 0; u < a; u++) {
                    var h = e.isDark(c, u), f = u * o, p = c * i;
                    r.strokeStyle = h ? n.colorDark : n.colorLight, r.lineWidth = 1, r.fillStyle = h ? n.colorDark : n.colorLight, r.fillRect(f, p, o, i), r.strokeRect(Math.floor(f) + .5, Math.floor(p) + .5, s, l), r.strokeRect(Math.ceil(f) - .5, Math.ceil(p) - .5, s, l)
                }
                this._bIsPainted = !0
            }, a.prototype.makeImage = function () {
                this._bIsPainted && t.call(this, e)
            }, a.prototype.isPainted = function () {
                return this._bIsPainted
            }, a.prototype.clear = function () {
                this._oContext.clearRect(0, 0, this._elCanvas.width, this._elCanvas.height), this._bIsPainted = !1
            }, a.prototype.round = function (e) {
                return e ? Math.floor(1e3 * e) / 1e3 : e
            }, a
        }() : function () {
            var e = function (e, t) {
                this._el = e, this._htOption = t
            };
            return e.prototype.draw = function (e) {
                for (var t = this._htOption, r = this._el, n = e.getModuleCount(), a = Math.floor(t.width / n), o = Math.floor(t.height / n), i = ['<table style="border:0;border-collapse:collapse;">'], s = 0; s < n; s++) {
                    i.push("<tr>");
                    for (var l = 0; l < n; l++) i.push('<td style="border:0;border-collapse:collapse;padding:0;margin:0;width:' + a + "px;height:" + o + "px;background-color:" + (e.isDark(s, l) ? t.colorDark : t.colorLight) + ';"></td>');
                    i.push("</tr>")
                }
                i.push("</table>"), r.innerHTML = i.join("");
                var c = r.childNodes[0], u = (t.width - c.offsetWidth) / 2, h = (t.height - c.offsetHeight) / 2;
                u > 0 && h > 0 && (c.style.margin = h + "px " + u + "px")
            }, e.prototype.clear = function () {
                this._el.innerHTML = ""
            }, e
        }();
    return c = function (e, t) {
        if (this._htOption = {
            width: 256,
            height: 256,
            typeNumber: 4,
            colorDark: "#000000",
            colorLight: "#ffffff",
            correctLevel: h.H
        }, "string" == typeof t && (t = {text: t}), t) for (var r in t) this._htOption[r] = t[r];
        "string" == typeof e && (e = document.getElementById(e)), this._htOption.useSVG && (w = v), this._android = i(), this._el = e, this._oQRCode = null, this._oDrawing = new w(this._el, this._htOption), this._htOption.text && this.makeCode(this._htOption.text)
    }, c.prototype.makeCode = function (e) {
        this._oQRCode = new t(s(e, this._htOption.correctLevel), this._htOption.correctLevel), this._oQRCode.addData(e), this._oQRCode.make(), this._el.title = e, this._oDrawing.draw(this._oQRCode), this.makeImage()
    }, c.prototype.makeImage = function () {
        "function" == typeof this._oDrawing.makeImage && (!this._android || this._android >= 3) && this._oDrawing.makeImage()
    }, c.prototype.clear = function () {
        this._oDrawing.clear()
    }, c.CorrectLevel = h, c
}), function (e, t) {
    "function" == typeof define && define.amd ? define("statisticEvent", [], t) : "object" == typeof exports ? module.exports = t() : e.statisticEvent = t()
}(window, function () {
    var e = {HIIDO_INTERNAL: "//hdjs.hiido.com/hiido_internal.js", WEBSDK: "//cdn.hiido.com/sdk/websdk.js"},
        t = "2.2.0", r = window.jQuery || window.$, n = window.hiidoEvent, a = {libReady: !1, holds: []}, o = {
            makeArray: function (e) {
                return Array.prototype.slice.call(e)
            }, cookies: {
                get: function (e) {
                    var t = document.cookie.match(new RegExp("(^| )" + e + "=([^;]*)(;|$)"));
                    return null !== t ? window.unescape(t[2]) : null
                }
            }, typeFn: function (e) {
                var t, r = Object.prototype.toString;
                return null === e ? t = String(e) : (t = r.call(e).toLowerCase(), t = t.substring(8, t.length - 1)), t
            }, isPlainObjectFn: function (e) {
                var t, r = this, n = Object.prototype.hasOwnProperty;
                if (!e || "object" !== r._type(e)) return !1;
                if (e.constructor && !n.call(e, "constructor") && !n.call(e.constructor.prototype, "isPrototypeOf")) return !1;
                for (t in e) ;
                return void 0 === t || n.call(e, t)
            }, getFromFn: function (e) {
                var t, r, n, a = {}, o = window.location.search, i = "";
                if (o) {
                    o = o.slice(1, o.length), t = o.split("&"), r = t.length;
                    for (var s = 0; s < r; s++) n = t[s], a[n.split("=")[0]] = n.split("=")[1]
                }
                return e = e || "f", e in a && (i = a[e]), i
            }, helpFn: function () {
            }
        }, i = {
            _type: o.typeFn,
            _isPlainObject: o.isPlainObjectFn,
            _getFrom: o.getFromFn,
            _version: t,
            help: o.help,
            _prodid: "yylive",
            _getRef: encodeURIComponent(window.document.referrer) || "",
            _config: {act_type: "", more_info: {web_type: "yy.com", module: "", moduleid: "", tabid: ""}, report_type: 0},
            _extend: function () {
                var e, t, r, n, a, o, i = this, s = arguments[0] || {}, l = 1, c = arguments.length, u = !1;
                for ("boolean" == typeof s && (u = s, s = arguments[1] || {}, l = 2), "object" != typeof s && "function" !== i._type(s) && (s = {}), c === l && (s = this, --l); l < c; l++) if (null !== (e = arguments[l])) for (t in e) r = s[t], n = e[t], s !== n && (u && n && (i._isPlainObject(n) || (a = "array" === i._type(n))) ? (a ? (a = !1, o = r && "array" === i._type(r) ? r : []) : o = r && i._isPlainObject(r) ? r : {}, s[t] = i._extend(u, o, n)) : void 0 !== n && (s[t] = n));
                return s
            },
            _set: function (e) {
                if (!e) throw new Error("statisticEvent.set() requires [options] params. ");
                if ("object" !== this._type(e)) throw new Error("param in statisticEvent.set() requires [Object] type.");
                if (!e.eventid) throw new Error("statisticEvent.emit() requires eventid. ");
                var t = {};
                this._config.from = this._getFrom(), this._config.ref = this._getRef, t = this._extend({}, this._config, e), this.emit(t.prodid || this._prodid, t.eventid, t)
            },
            _emit: function (e, t, r) {
                var a = new n(e, t);
                switch (a.setActtype(r.act_type), a.setFrom(r.from), a.setRef(r.ref), a.setMoreinfo(r.more_info), a.setUid(o.cookies.get("yyuid") || ""), a.setSid(r.sid), a.setSys("4"), r.report_type) {
                    case 0:
                        a.reportJudge();
                        break;
                    case 1:
                        a.reportProcess();
                        break;
                    case 2:
                        a.reportAmount();
                        break;
                    case 3:
                        a.reportHeart()
                }
            },
            _eventInit: function (e, t) {
                var n = this;
                t = t || {}, r(e).on("click", function (e) {
                    e = e.originalEvent;
                    for (var a, o, i, s = e.target || e.srcElement, l = this, c = !1, u = n._extend({}, n._config.more_info, t.more_info), h = "data-statistic-"; s;) {
                        i = r(s).attr(h + "through");
                        for (var f in u) u.hasOwnProperty(f) && (a = h + f.replace(/_/g, "-"), o = r(s).attr(a), o && (u[f] = o, i || (c = !0)));
                        if (s == l || u.moduleid) break;
                        s = s.parentNode
                    }
                    if (c) try {
                        u && u.module && (t.onsend && (u = t.onsend(u)), n.set({eventid: t.eventid, more_info: u}))
                    } catch (p) {
                    }
                })
            },
            init: function (t) {
                var o = function () {
                    r(a.holds).each(function (e, t) {
                        var r = t[0], n = t[1], a = t[2] || [];
                        n && "function" == typeof r && r.apply(n, a)
                    }), a.holds = []
                };
                return n ? (a.libReady = !0, o(), t && t()) : void r.getScript(e.HIIDO_INTERNAL, function () {
                    r.getScript(e.WEBSDK, function () {
                        return n = window.hiidoEvent, a.libReady = !0, o(), t && t()
                    })
                })
            },
            set: function () {
                var e = this, t = o.makeArray(arguments);
                a.libReady ? e._set.apply(e, t) : a.holds.push([e._set, e, t])
            },
            emit: function () {
                var e = this, t = o.makeArray(arguments);
                a.libReady ? e._emit.apply(e, t) : a.holds.push([e._emit, t])
            },
            eventInit: function () {
                var e = this, t = o.makeArray(arguments);
                a.libReady ? e._eventInit.apply(e, t) : a.holds.push([e._eventInit, t])
            }
        };
    return i
}), define("paymentDialog", ["util", "artTemplate", "QRCode", "statisticEvent"], function (e, t, r, n) {
    function a(e, t, r) {
        return function () {
            s(e, t, r)
        }
    }

    function o() {
        var e = u;
        $("#qrcode-img").html(e.qrloadingTxt)
    }

    function i(e) {
        var t = u;
        e ? $("#qrcode-img").html('<div class="qrFailTxt">{$msg}</div>'.replace("{$msg}", e)) : $("#qrcode-img").html(t.qrFailTxt), t.statistic(1006), t.isFinishRenderQr = !0
    }

    function s(e, r, n) {
        var a = u, o = {}, s = "";
        "YC" === n ? s = "//www.yy.com/show/qr/getOrderSts.action" : "RD" === n && (s = "//www.yy.com/show/pay/getOrderSts.action"), $.ajax({
            url: s,
            type: "post",
            dataType: "json",
            data: {appOrderId: e, createDate: r},
            error: function () {
                i()
            },
            success: function (r) {
                "YC" === n ? 0 == r.result ? r.statusCode && (o.date = (new Date).format("yyyy-MM-dd hh:mm:ss"), o.appOrderId = e, o.amount = a.amount, o.yyNum = a.userInfo && a.userInfo.yynum, o.nick = a.userInfo.nick, o.type = a.rechargeType.map[a.rechargeType.current] || "", "2" == r.statusCode ? (clearInterval(a.timeInterval), $("#qr-tab2").html(t("successTmp", o)), a.changeTab(1), a.RechargeCallBack(), a.statistic(1008)) : "3" == r.statusCode && (clearInterval(a.timeInterval), o.amount = 0, $("#qr-tab3").html(t("failTmp", o)), a.changeTab(2))) : (clearInterval(a.timeInterval), o.amount = 0, $("#qr-tab3").html(t("failTmp", o)), a.changeTab(2)) : "RD" === n && (r.orderStatus ? (o.date = (new Date).format("yyyy-MM-dd hh:mm:ss"), o.appOrderId = e, o.amount = r.diamondAmount, o.yyNum = a.userInfo && a.userInfo.yynum, o.nick = a.userInfo.nick, o.type = a.rechargeType.map[a.rechargeType.current] || "", "2" == r.orderStatus || "4" == r.orderStatus ? (clearInterval(a.timeInterval), $("#qr-tab2").html(t("successTmp", o)), a.changeTab(1), a.RechargeCallBack(), a.statistic(1008)) : "8" == r.orderStatus && (clearInterval(a.timeInterval), o.amount = 0, $("#qr-tab3").html(t("failTmp", o)), a.changeTab(2))) : (clearInterval(a.timeInterval), o.amount = 0, $("#qr-tab3").html(t("failTmp", o)), a.changeTab(2)))
            }
        })
    }

    console.log("dev works"), Date.prototype.format = function (e) {
        var t = {
            "M+": this.getMonth() + 1,
            "d+": this.getDate(),
            "h+": this.getHours(),
            "m+": this.getMinutes(),
            "s+": this.getSeconds(),
            "q+": Math.floor((this.getMonth() + 3) / 3),
            S: this.getMilliseconds()
        };
        /(y+)/.test(e) && (e = e.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length)));
        for (var r in t) new RegExp("(" + r + ")").test(e) && (e = e.replace(RegExp.$1, 1 == RegExp.$1.length ? t[r] : ("00" + t[r]).substr(("" + t[r]).length)));
        return e
    };
    var l = {}, c = 20021911, u = {
        timeInterval: 0,
        intervalID: 0,
        amount: 10,
        balance: 0,
        userInfo: {},
        ENV: null,
        simple: null,
        rechargeType: {map: {YC: "Y币", RD: "红钻"}, current: "YC"},
        isFinishRenderQr: !1,
        qrloadingTxt: ['<div class="loadingStatus"></div>'].join(""),
        qrFailTxt: ['<div class="qrFailTxt">', '<p class="qrFailTxt-top">二维码失效</p>', '<p>请点击<a class="reloadQrCode" href="javascript:;">刷新</a></p>', "</div>"].join(""),
        rechargeCallBacks: null,
        closeRechargeCallBacks: null,
        init: function (t) {
            var r = u, a = e.getParameterByName("callback", window.location.href);
            r.rechargeType.current = e.getParameterByName("type", window.location.href), r.simple = e.getParameterByName("simple", window.location.href), r.ENV = "dev" === e.getParameterByName("env", window.location.href), t && $(t).append($("#qr-payment")), l.hasRender || (r.bindEvent(), r.getBalance(), l.hasRender = !0), "makeSure" === e.getParameterByName("tab", window.location.href) ? r.makeSureBox() : r.showQrBox(e.getParameterByName("total", window.location.href), e.getParameterByName("scenceType", window.location.href)), a && "function" == typeof window.parent[a] && r.addCloseRechargeCallbacks(function () {
                if (window.parent[a](), window.parent[a] = null, window.parent !== window) {
                    var e = window.parent.document, t = e.getElementById("paymentIframe");
                    t.parentNode.removeChild(t)
                }
            }), r.addRechargeCallbacks(function () {
                n.set({eventid: "20016765", act_type: "5006"})
            })
        },
        bindEvent: function () {
            var e = u;
            $(".payment-main").on("click", ".head-close,.delet-recharge", function (t) {
                if (t.stopPropagation(), e.closeRechargeCallBack(), e.statistic(1003), window.parent !== window) {
                    var r = window.parent.document, n = r.getElementById("paymentIframe");
                    n.parentNode.removeChild(n)
                }
            }), $(".payment-main").on("click", ".select-money a", function (t) {
                t.stopPropagation(), e.amount = $(this).data("type"), $("#qr-input-amount").val("其他面额"), $("#qr-tips").css("display", "none"), $(".select-money").removeClass("selecte-focus"), $(".select-money a").removeClass("selected"), $(".select-money a[data-type=" + e.amount + "]").addClass("selected"), $(".money-amount-count").html(e.amount), e.getQrAndRecharge()
            }), $(".payment-main").on("click", ".continue-recharge", function () {
                e.showQrBox(), e.statistic(1002)
            }), $(".payment-main").on("click", "#qr-confirm", function () {
                e.isFinishRenderQr && e.checkInput() && ($(".money-amount-count").html(e.amount), e.getQrAndRecharge())
            }), $(".payment-main").on("click", "#open-recharge", function () {
                e.statistic(1007), window.open("//pay.duowan.com/userDepositDWAction.action")
            }), $(".payment-main").on("click", ".reloadQrCode", function () {
                var e = u;
                o(), e.getQrAndRecharge(), e.statistic(1005)
            }), $(".payment-main").on("focus", "#qr-input-amount", function () {
                var e = u;
                $(".select-money").addClass("selecte-focus"), e.amount && "其他面额" != $("#qr-input-amount").val() || ($("#qr-input-amount").val(""), e.inputAmountFn(""))
            }).bind("input propertychange", function () {
                "" != $("#qr-input-amount").val() ? $("#qr-confirm").addClass("inputVal") : $("#qr-confirm").removeClass("inputVal")
            }).bind("keyup", "#qr-input-amount", function (e) {
                13 == e.keyCode && $("#qr-confirm").trigger("click")
            })
        },
        statistic: function (e) {
            n.set({eventid: c, act_type: e, more_info: {frame_type: 1}})
        },
        getBalance: function () {
            var t = u;
            $.ajax({
                url: "//www.yy.com/zone/assets/total.json", dataType: "json", type: "get", success: function (r) {
                    r.code || (t.balance = "YC" === t.rechargeType.current ? e.thousandSeparator(r.dwb / 100, 2) : e.thousandSeparator(r.hz))
                }, error: function () {
                }
            })
        },
        inputAmountFn: function (e) {
            $("#qr-ten").removeClass("selected"), $("#qr-fifty").removeClass("selected"), $("#qr-hundred").removeClass("selected"), $(".select-money").addClass("selecte-focus"), $("#qr-input-amount").val(e), $("#qr-confirm").show(), $("#qr-confirm").addClass("inputVal")
        },
        commonOp: function (e, t) {
            var r = u;
            $("#qr-input-amount").val("其他金额"), (r.amount != e || t) && (r.amount = e, $(".payment-main .money-amount-count").html(r.amount), r.getQrAndRecharge())
        },
        checkInput: function () {
            var e = u, t = $("#qr-input-amount").val(), r = /^\d+$/;
            return e.ENV ? (e.amount = t, $("#qr-tips").css("display", "none"), !0) : !r.test(t) || t < 1 || t > 2e3 ? ($("#qr-tips").css("display", "block"), !1) : e.amount != t && (e.amount = t, $("#qr-tips").css("display", "none"), !0)
        },
        makeSureBox: function () {
            var e = u;
            e.changeTab(3), $("#qr-tab4").html(t("makesureTpl", {})), e.statistic(1001)
        },
        showQrBox: function (e, r, n) {
            var a = u, o = "1" == a.simple ? "head usercenter-head" : "head",
                i = '<div class="payment-dialog-loading"><div class="' + o + '"><a id="qr-tab1-close" class="head-close" href="javascript:void(0);" title="点击关闭"></a></div></div>';
            $("#qr-content-mask").show(), $("#qr-tab1").html(i).css("display", "block"), $.ajax({
                url: "//www.yy.com/zone/userinfo/qryUserInfo.json",
                dataType: "json",
                type: "get",
                success: function (o) {
                    o.code || (a.userInfo = o.data, "function" == typeof e && (n = e, e = void 0), a.changeTab(0), $("#qr-tab1").html(t("qrBoxTpl", {
                        nick: a.userInfo.nick || "-",
                        amount: a.balance,
                        type: a.rechargeType.map[a.rechargeType.current] || "",
                        simple: a.simple
                    })), a.statistic(1004), e > 2e3 ? ($("#below-qr-tips").text("二维码充值每日限额2000，打开页面充值"), e = 2e3) : $("#below-qr-tips").text("手机微信或支付扫码支付"), e ? $("#qr-payment").addClass("payment-main--hideselect") : ($("#qr-payment").removeClass("payment-main--hideselect"), e = 10), 10 == e || 50 == e || 100 == e ? ($(".select-money a").removeClass("selected"), $(".select-money a[data-type=" + e + "]").addClass("selected"), a.amount = e, $(".money-amount-count").html(a.amount), a.getQrAndRecharge(r), "function" == typeof n && a.addRechargeCallbacks(n)) : (a.inputAmountFn(e), a.checkInput() && ($(".money-amount-count").html(a.amount), a.getQrAndRecharge(r), "function" == typeof n && a.addRechargeCallbacks(n))), $.ajax({
                        url: "//ysapi.yy.com/api/internal/moneyquery/getiaptips.json",
                        dataType: "jsonp",
                        type: "get",
                        data: {data: JSON.stringify({accounttype: 0, srctype: "yycomcharge"})},
                        success: function (e) {
                            e.result || $(".live-recharge-tips").eq(0).html(e.iaptips)
                        },
                        error: function () {
                        }
                    }))
                },
                error: function () {
                }
            })
        },
        hideQrBox: function () {
            var e = u;
            $("#qr-content-mask").hide(), e.changeTab(-1)
        },
        closeTab1: function () {
            var e = u;
            $("#qr-tab1").hide(), $("#qr-tab2").hide(), $("#qr-tab3").hide(), e.amount = 10, $("#qr-content-mask").hide(), clearInterval(e.timeInterval), e.closeRechargeCallBack()
        },
        RechargeCallBack: function () {
            if (null != u.rechargeCallBacks) for (var t = u.rechargeCallBacks.length, r = 0; r < t; r++) {
                var n = u.rechargeCallBacks[r];
                n(), e.trace.info("w-payment", "充值成功 回调业务函数fn=", n)
            }
        },
        addRechargeCallbacks: function (e) {
            null == u.rechargeCallBacks && (u.rechargeCallBacks = new Array), u.rechargeCallBacks.push(e)
        },
        closeRechargeCallBack: function () {
            if (null != u.closeRechargeCallBacks) for (var t = u.closeRechargeCallBacks.length, r = 0; r < t; r++) {
                var n = u.closeRechargeCallBacks[r];
                n(), e.trace.info("w-payment", "关闭充值窗口 回调业务函数fn=", n)
            }
            u.rechargeCallBacks = null
        },
        addCloseRechargeCallbacks: function (e) {
            null == u.closeRechargeCallBacks && (u.closeRechargeCallBacks = new Array), u.closeRechargeCallBacks.push(e)
        },
        changeTab: function (e) {
            $("#qr-payment .tab").css("display", "none"), $("#qr-payment .tab").eq(e).css("display", "block")
        },
        getQrAndRecharge: function (t) {
            var n, o = u;
            o.isFinishRenderQr = !1, clearTimeout(o.intervalID), o.intervalID = setTimeout(function () {
                u.isFinishRenderQr = !0
            }, 15e3), $("#qrcode-img").html('<div class="recharge-qrcode-loading"><div class="recharge-qrcode-img"></div><div class="recharge-qrcode-txt">二维码加载中</div></div>'), "YC" === o.rechargeType.current ? n = "//www.yy.com/show/qr/getOrderId.action" : "RD" === o.rechargeType.current && (n = "//www.yy.com/show/pay/getOrderId.action"), $.ajax({
                url: n,
                type: "post",
                async: !1,
                dataType: "json",
                data: {},
                timeout: 5e4,
                error: function (t, r, n) {
                    e.trace.info("w-payment", "w-payment:252", t, r, n), clearTimeout(o.intervalID), i()
                },
                success: function (n) {
                    if (n && n.appOrderId) {
                        var s = n.appOrderId, l = {}, c = "", u = "";
                        if (void 0 == s || "" == s) return;
                        "RD" === o.rechargeType.current ? (l = {
                            appOrderId: s,
                            payMoney: o.amount,
                            bankId: "paygage",
                            payType: "0",
                            cardNum: "",
                            cardPass: "",
                            cpuid: 0,
                            channelId: 0,
                            srcType: "",
                            bizType: ""
                        }, c = "//www.yy.com/show/pay/redDiamondQRPay.action", u = "RD") : "YC" === o.rechargeType.current && (l = {
                            appOrderId: s,
                            payMoney: o.amount,
                            scenceType: t
                        }, c = "//www.yy.com/show/qr/qrRecharge.action", u = "YC"), $.ajax({
                            url: c,
                            type: "post",
                            dataType: "json",
                            data: l,
                            error: function (t) {
                                e.trace.info("w-payment", t), i()
                            },
                            success: function (t) {
                                if (clearInterval(o.timeInterval), t && 0 == t.result) {
                                    var n = parseFloat(t.amount), l = t.createDate || "",
                                        c = "YC" === u ? t.urlPay : t.payUrl;
                                    if (o.amount == n) {
                                        $("#qrcode-img").empty();
                                        var h = {width: 128, height: 128},
                                            f = new r(document.getElementById("qrcode-img"), h);
                                        f.makeCode(c), o.isFinishRenderQr = !0, clearTimeout(o.intervalID), o.timeInterval = setInterval(a(s, l, u), 3e3)
                                    }
                                } else t && t.result == -9999 ? i("登录已失效,请重新登录") : (e.trace.info("w-payment", "w-payment:296", t), i())
                            }
                        })
                    } else i()
                }
            })
        }
    };
    return u
}), require(["paymentDialog"], function (e) {
    e.init()
}), define("components/p-payment/p-index.js", function () {
});