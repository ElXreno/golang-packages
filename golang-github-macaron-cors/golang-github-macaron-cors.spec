%global goipath         github.com/go-macaron/cors
%global commit          6fd6a9bfe14e9ed6ddf9265b6580f7638105b27b
%global scm             git

%gometa

%global common_description %{expand:
Middleware that handles CORS requests & headers for Macaron.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware that handles CORS requests & headers for Macaron.

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
